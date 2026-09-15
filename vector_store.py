from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document
import faiss
from pathlib import Path
import pickle

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embeddings(self, chunks: list[Document]):
        return self.model.encode([chunk.page_content for chunk in chunks])
    
    def build_index(self, embeddings):
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        return index
    
    def search_index(self, index, query_embedding, top_k=5):
        distances, indices = index.search(query_embedding, top_k)
        return distances, indices
    
    def save_index(self, index, path="storage/faiss.index"):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(index, str(path))
        
    def load_index(self, path="storage/faiss.index"):
        return faiss.read_index(str(path))
    
    def save_chunks(self, chunks: list[Document], path="storage/chunks.pkl"):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as file:
            pickle.dump(chunks, file)
            
    def load_chunks(self, path="storage/chunks.pkl"):
        with open(path, "rb") as file:
            return pickle.load(file)