from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

class RAGRetriever:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        # Initialize the embedding model
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vector_store = None

    def build_index(self, chunks):
        # Handle both plain text lists and dictionary chunks with metadata
        if isinstance(chunks[0], dict):
            texts = [c["text"] for c in chunks]
            metadatas = [{"section": c.get("section", "General")} for c in chunks]
        else:
            texts = chunks
            metadatas = None

        # Build FAISS vector store from texts
        self.vector_store = FAISS.from_texts(texts, self.embeddings, metadatas=metadatas)

    def retrieve(self, query: str, k: int = 3):
        if not self.vector_store:
            raise ValueError("Vector store has not been built yet! Call build_index first.")
        
        # Search the vector store for the top k most similar chunks
        docs = self.vector_store.similarity_search_with_score(query, k=k)
        
        results = []
        for doc, score in docs:
            results.append({
                "text": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            })
        return results
