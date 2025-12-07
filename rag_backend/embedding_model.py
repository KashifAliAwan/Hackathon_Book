"""
Embedding model module for the RAG system.
Handles text embedding generation using free-tier compatible models.
"""
from typing import List, Union, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os


class EmbeddingModel:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", api_key: Optional[str] = None):
        """
        Initialize the embedding model.

        Args:
            model_name: Name of the embedding model to use
                      For free-tier: "all-MiniLM-L6-v2", "all-mpnet-base-v2", etc.
                      For Gemini: "text-embedding-004" (requires API key)
            api_key: API key for cloud-based embedding services (e.g., Gemini)
        """
        self.model_name = model_name
        self.api_key = api_key
        self.model = None
        self.is_gemini = "gemini" in model_name.lower() or "text-embedding" in model_name.lower()

        if self.is_gemini and api_key:
            genai.configure(api_key=api_key)
            self.model = genai.embed_content(
                model=model_name,
                content=["test"],  # Test call to verify model access
                task_type="retrieval_document"
            )
            print(f"Initialized Gemini embedding model: {model_name}")
        elif not self.is_gemini:
            # Use local sentence-transformers model
            self.model = SentenceTransformer(model_name)
            print(f"Initialized local embedding model: {model_name}")
        else:
            raise ValueError("API key required for Gemini embedding models")

    def embed_text(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Input text to embed

        Returns:
            Embedding vector as a list of floats
        """
        if self.is_gemini:
            result = genai.embed_content(
                model=self.model_name,
                content=[text],
                task_type="retrieval_document"
            )
            return result['embedding'][0]  # Return the first (and only) embedding
        else:
            embedding = self.model.encode([text])
            return embedding[0].tolist()  # Convert numpy array to list

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of input texts to embed

        Returns:
            List of embedding vectors (each as a list of floats)
        """
        if self.is_gemini:
            result = genai.embed_content(
                model=self.model_name,
                content=texts,
                task_type="retrieval_document"
            )
            return [emb.tolist() for emb in result['embedding']]
        else:
            embeddings = self.model.encode(texts)
            return [emb.tolist() for emb in embeddings]

    def get_embedding_dimension(self) -> int:
        """
        Get the dimension of the embeddings produced by this model.

        Returns:
            Dimension of the embedding vectors
        """
        if self.is_gemini:
            # Common dimensions for Gemini embedding models
            if "004" in self.model_name:
                return 768  # text-embedding-004 typically has 768 dimensions
            else:
                return 768  # Default assumption
        else:
            # For sentence-transformers models
            test_embedding = self.model.encode(["test"])
            return test_embedding.shape[1]


class TextChunker:
    """
    Utility class for chunking text into smaller pieces suitable for embedding.
    """
    def __init__(self, chunk_size: int = 512, overlap: int = 50):
        """
        Initialize the text chunker.

        Args:
            chunk_size: Maximum number of tokens per chunk
            overlap: Number of overlapping tokens between chunks
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str, chunk_by: str = "sentence") -> List[str]:
        """
        Split text into chunks.

        Args:
            text: Input text to chunk
            chunk_by: Method to use for chunking ("sentence", "word", "char", "token")

        Returns:
            List of text chunks
        """
        if chunk_by == "sentence":
            return self._chunk_by_sentence(text)
        elif chunk_by == "word":
            return self._chunk_by_word(text)
        elif chunk_by == "char":
            return self._chunk_by_char(text)
        else:
            # Default to sentence-based chunking
            return self._chunk_by_sentence(text)

    def _chunk_by_sentence(self, text: str) -> List[str]:
        """Chunk text by sentences."""
        import re

        # Split text into sentences
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        chunks = []
        current_chunk = ""
        current_length = 0

        for sentence in sentences:
            # Add some punctuation back for better context
            sentence_with_punct = sentence.strip() + "."

            # Estimate token count (rough approximation: 1 token ~ 4 chars)
            sentence_tokens = len(sentence_with_punct.split())

            if current_length + sentence_tokens > self.chunk_size and current_chunk:
                chunks.append(current_chunk.strip())
                # Start a new chunk with potential overlap
                current_chunk = sentence_with_punct
                current_length = sentence_tokens
            else:
                current_chunk += " " + sentence_with_punct
                current_length += sentence_tokens

        # Add the last chunk if it has content
        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        # Handle overlap by adding overlapping content
        if self.overlap > 0 and len(chunks) > 1:
            chunks = self._add_overlap(chunks)

        return chunks

    def _chunk_by_word(self, text: str) -> List[str]:
        """Chunk text by words."""
        words = text.split()
        chunks = []

        for i in range(0, len(words), self.chunk_size - self.overlap):
            chunk_words = words[i:i + self.chunk_size]
            chunks.append(" ".join(chunk_words))

        return chunks

    def _chunk_by_char(self, text: str) -> List[str]:
        """Chunk text by characters."""
        chunks = []

        for i in range(0, len(text), self.chunk_size * 4 - self.overlap * 4):  # Approximate char-to-token ratio
            chunk_text = text[i:i + self.chunk_size * 4]
            chunks.append(chunk_text.strip())

        return chunks

    def _add_overlap(self, chunks: List[str]) -> List[str]:
        """Add overlap between chunks."""
        if len(chunks) <= 1 or self.overlap == 0:
            return chunks

        overlapped_chunks = []
        for i, chunk in enumerate(chunks):
            if i == 0:
                overlapped_chunks.append(chunk)
            else:
                # Get the last few words from the previous chunk for overlap
                prev_words = chunks[i-1].split()[-self.overlap:]
                overlap_text = " ".join(prev_words)
                overlapped_chunk = overlap_text + " " + chunk
                overlapped_chunks.append(overlapped_chunk)

        return overlapped_chunks


# Example usage and testing
if __name__ == "__main__":
    # Example with local model (free-tier compatible)
    local_model = EmbeddingModel(model_name="all-MiniLM-L6-v2")

    # Test embedding
    test_text = "This is a test sentence for embedding."
    embedding = local_model.embed_text(test_text)
    print(f"Embedding dimension: {len(embedding)}")
    print(f"Sample embedding values: {embedding[:5]}...")

    # Example text chunking
    chunker = TextChunker(chunk_size=100, overlap=20)
    sample_text = "This is a longer text that will be split into multiple chunks. " * 10
    chunks = chunker.chunk_text(sample_text)
    print(f"Number of chunks created: {len(chunks)}")
    print(f"First chunk: {chunks[0][:100]}...")