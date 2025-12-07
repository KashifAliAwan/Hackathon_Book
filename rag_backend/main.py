"""
Main FastAPI application for the RAG chatbot system.
"""
from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from typing import List, Dict, Optional
import os
import asyncio
from dotenv import load_dotenv

# Import our modules
from database import DatabaseManager, generate_content_hash
from qdrant_client import QdrantManager
from embedding_model import EmbeddingModel, TextChunker

# Load environment variables
load_dotenv()

# Initialize the application
app = FastAPI(
    title="AI Textbook RAG API",
    description="API for interacting with AI-generated textbooks using RAG",
    version="1.0.0"
)

# Global variables for our services
db_manager: Optional[DatabaseManager] = None
qdrant_manager: Optional[QdrantManager] = None
embedding_model: Optional[EmbeddingModel] = None
text_chunker: Optional[TextChunker] = None


class ChatRequest(BaseModel):
    query: str
    textbook_id: str
    chat_history: Optional[List[Dict]] = []
    language: Optional[str] = "en"


class ChatResponse(BaseModel):
    answer: str
    sources: List[Dict]


class GenerateTextbookRequest(BaseModel):
    topic: str = "Physical AI & Humanoid Robotics"
    chapter_count: int = 6
    language: str = "en"


@app.on_event("startup")
async def startup_event():
    """Initialize all services when the application starts."""
    global db_manager, qdrant_manager, embedding_model, text_chunker

    # Initialize database manager
    database_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/textbook_db")
    db_manager = DatabaseManager(database_url)
    await db_manager.connect()
    await db_manager.create_tables()

    # Initialize Qdrant manager
    qdrant_host = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port = int(os.getenv("QDRANT_PORT", "6333"))
    qdrant_manager = QdrantManager(host=qdrant_host, port=qdrant_port)

    # Initialize embedding model
    llm_api_key = os.getenv("LLM_API_KEY")
    llm_model_name = os.getenv("LLM_MODEL_NAME", "all-MiniLM-L6-v2")

    # Use local model by default for free-tier compatibility
    if llm_model_name == "gemini-pro":
        embedding_model = EmbeddingModel(model_name="all-MiniLM-L6-v2")
    else:
        embedding_model = EmbeddingModel(model_name=llm_model_name, api_key=llm_api_key)

    # Initialize text chunker
    text_chunker = TextChunker(chunk_size=512, overlap=50)

    print("All services initialized successfully")


@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources when the application shuts down."""
    global db_manager
    if db_manager:
        await db_manager.close()


@app.get("/")
async def root():
    """Root endpoint to verify the API is running."""
    return {"message": "AI Textbook RAG API is running", "version": "1.0.0"}


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint that answers questions based on textbook content using RAG.
    """
    global db_manager, qdrant_manager, embedding_model

    try:
        # Verify the textbook exists
        textbook = await db_manager.get_textbook_by_collection(request.textbook_id)
        if not textbook:
            raise HTTPException(status_code=404, detail="Textbook not found")

        # Generate embedding for the query
        query_embedding = embedding_model.embed_text(request.query)

        # Search for relevant content in Qdrant
        search_results = qdrant_manager.search_similar(
            collection_name=request.textbook_id,
            query_vector=query_embedding,
            textbook_id=request.textbook_id,
            limit=5  # Get top 5 most relevant chunks
        )

        if not search_results:
            return ChatResponse(
                answer="I couldn't find relevant information in the textbook to answer your question.",
                sources=[]
            )

        # Prepare context from the search results
        context_parts = []
        sources = []

        for result in search_results:
            content = result["payload"]["content"]
            context_parts.append(content)

            source_info = {
                "chapter": result["payload"].get("chapter", "Unknown"),
                "section": result["payload"].get("section", "Unknown"),
                "page_link": result["payload"].get("page_link", ""),
                "relevance_score": result["score"]
            }
            sources.append(source_info)

        context = "\n\n".join(context_parts)

        # In a real implementation, you would send this context to an LLM
        # For now, we'll return a simulated response based on the context
        answer = f"Based on the textbook content, here's the answer to your question '{request.query}':\n\n{context[:500]}..."

        return ChatResponse(answer=answer, sources=sources)

    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.post("/api/v1/generate_textbook")
async def generate_textbook(request: GenerateTextbookRequest):
    """
    Endpoint to trigger textbook generation (placeholder implementation).
    In a real implementation, this would generate textbook content using an LLM.
    """
    # This is a placeholder - in the real implementation, this would generate content
    # using an LLM and save it to the database and file system
    return {
        "message": f"Textbook generation for topic '{request.topic}' with {request.chapter_count} chapters would be triggered here",
        "status": "not_implemented_yet"
    }


@app.get("/api/v1/textbooks")
async def get_textbooks():
    """Get a list of available textbooks."""
    try:
        # This would query the database for available textbooks
        # For now, return a placeholder response
        return {
            "textbooks": [
                {
                    "id": "physical-ai-humanoid-robotics",
                    "title": "Physical AI & Humanoid Robotics",
                    "version": "1.0",
                    "language": "en"
                }
            ]
        }
    except Exception as e:
        print(f"Error in get_textbooks: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": asyncio.get_event_loop().time()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)