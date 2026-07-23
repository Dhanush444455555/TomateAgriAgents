"""RAG Search Tool - Searches vector store for relevant agronomic knowledge."""
from app.rag.vector_store import VectorStore


class RAGSearchTool:
    """Searches the agronomic knowledge base for relevant passages.
    
    Used by: ALL agents for grounding their LLM reasoning.
    Returns: relevant text passages with source attribution.
    """
    
    name = "rag_search"
    description = "Search the agricultural knowledge base for information relevant to a query"
    
    def __init__(self):
        self.vector_store = VectorStore()
    
    async def execute(self, query: str, k: int = 5, filter_topic: str = None) -> dict:
        """Search vector store for relevant knowledge passages."""
        try:
            results = self.vector_store.query(query, k=k)
            return {
                "success": True,
                "passages": results,
                "query": query,
                "num_results": len(results),
                "source": "ChromaDB Knowledge Base"
            }
        except Exception as e:
            return {"success": False, "error": str(e), "passages": []}
