"""Shared multilingual embedding configuration for HTML ingestion and retrieval."""

from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

EMBEDDING_MODEL = "BAAI/bge-m3"
# Keep these vectors separate from the original MiniLM collection.
COLLECTION_NAME = "docs_bge_m3"


def embedding_function() -> SentenceTransformerEmbeddingFunction:
    return SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL,
        normalize_embeddings=True,
    )
