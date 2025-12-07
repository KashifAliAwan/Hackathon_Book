"""
Qdrant client module for the RAG system.
Handles vector database operations using Qdrant.
"""
from typing import List, Dict, Optional
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams
import uuid


class QdrantManager:
    def __init__(self, host: str = "localhost", port: int = 6333, api_key: Optional[str] = None, url: Optional[str] = None):
        if url:
            self.client = QdrantClient(url=url, api_key=api_key)
        else:
            self.client = QdrantClient(host=host, port=port, api_key=api_key)

    def create_collection(self, collection_name: str, vector_size: int = 384, distance: str = "Cosine"):
        """
        Create a new collection in Qdrant for storing embeddings.

        Args:
            collection_name: Name of the collection to create
            vector_size: Size of the embedding vectors (default 384 for sentence-transformers)
            distance: Distance metric for similarity search (Cosine, Euclid, Manhattan)
        """
        try:
            # Check if collection already exists
            collections = self.client.get_collections()
            existing_collections = [col.name for col in collections.collections]

            if collection_name not in existing_collections:
                # Create collection with specified vector size and distance metric
                self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(size=vector_size, distance=Distance[distance.upper()])
                )

                # Create payload index for textbook_id to enable filtering
                self.client.create_payload_index(
                    collection_name=collection_name,
                    field_name="textbook_id",
                    field_schema=models.PayloadSchemaType.KEYWORD
                )

                print(f"Created Qdrant collection: {collection_name}")
            else:
                print(f"Qdrant collection {collection_name} already exists")
        except Exception as e:
            print(f"Error creating Qdrant collection {collection_name}: {str(e)}")
            raise e

    def delete_collection(self, collection_name: str):
        """Delete a collection from Qdrant."""
        try:
            self.client.delete_collection(collection_name=collection_name)
            print(f"Deleted Qdrant collection: {collection_name}")
        except Exception as e:
            print(f"Error deleting Qdrant collection {collection_name}: {str(e)}")
            raise e

    def upsert_embeddings(self, collection_name: str, embeddings: List[Dict], vector_size: int = 384):
        """
        Upsert (insert or update) embeddings into the specified collection.

        Args:
            collection_name: Name of the collection to insert into
            embeddings: List of dictionaries containing:
                - id: Unique identifier for the chunk
                - vector: The embedding vector
                - payload: Dictionary with metadata (textbook_id, chapter_id, content, etc.)
        """
        try:
            points = []
            for item in embeddings:
                point = models.PointStruct(
                    id=item["id"],
                    vector=item["vector"],
                    payload=item["payload"]
                )
                points.append(point)

            self.client.upsert(
                collection_name=collection_name,
                points=points
            )
            print(f"Upserted {len(points)} embeddings to collection: {collection_name}")
        except Exception as e:
            print(f"Error upserting embeddings to collection {collection_name}: {str(e)}")
            raise e

    def search_similar(self, collection_name: str, query_vector: List[float],
                      textbook_id: Optional[str] = None, limit: int = 10) -> List[Dict]:
        """
        Search for similar embeddings in the specified collection.

        Args:
            collection_name: Name of the collection to search in
            query_vector: The query embedding vector
            textbook_id: Optional filter to search only within a specific textbook
            limit: Maximum number of results to return

        Returns:
            List of dictionaries containing similarity search results
        """
        try:
            # Prepare filters if textbook_id is provided
            filters = None
            if textbook_id:
                filters = models.Filter(
                    must=[
                        models.FieldCondition(
                            key="textbook_id",
                            match=models.MatchValue(value=textbook_id)
                        )
                    ]
                )

            # Perform the search
            search_results = self.client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                query_filter=filters,
                limit=limit
            )

            # Format results
            results = []
            for result in search_results:
                results.append({
                    "id": result.id,
                    "score": result.score,
                    "payload": result.payload,
                    "vector": result.vector if hasattr(result, 'vector') else None
                })

            return results
        except Exception as e:
            print(f"Error searching in collection {collection_name}: {str(e)}")
            raise e

    def get_collection_info(self, collection_name: str) -> Dict:
        """Get information about a collection."""
        try:
            info = self.client.get_collection(collection_name=collection_name)
            return {
                "name": info.config.params.vectors_count,
                "vector_count": info.vectors_count,
                "indexed_vectors_count": info.indexed_vectors_count,
                "points_count": info.points_count
            }
        except Exception as e:
            print(f"Error getting collection info for {collection_name}: {str(e)}")
            raise e

    def delete_points_by_textbook(self, collection_name: str, textbook_id: str):
        """Delete all points in a collection that belong to a specific textbook."""
        try:
            # Filter to match points with the specific textbook_id
            filter_condition = models.Filter(
                must=[
                    models.FieldCondition(
                        key="textbook_id",
                        match=models.MatchValue(value=textbook_id)
                    )
                ]
            )

            # Delete points matching the filter
            self.client.delete(
                collection_name=collection_name,
                points_selector=models.FilterSelector(
                    filter=filter_condition
                )
            )
            print(f"Deleted points for textbook {textbook_id} from collection {collection_name}")
        except Exception as e:
            print(f"Error deleting points for textbook {textbook_id} from collection {collection_name}: {str(e)}")
            raise e