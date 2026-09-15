from document_processor.processor import DocumentProcessor
from document_processor.chunker import DocumentChunker
from vector_store import VectorStore

# Load all documents from the data folder
processor = DocumentProcessor()
documents = processor.load_documents("data")

print(f"Number of documents: {len(documents)}")


# Split documents into chunks
chunker = DocumentChunker(chunk_size=500, chunk_overlap=50)
chunks = chunker.chunk_documents(documents)

print(f"Number of chunks: {len(chunks)}")


# Create VectorStore
vector_store = VectorStore()

# Create embeddings for chunks
embeddings = vector_store.create_embeddings(chunks)
print(f"Embeddings shape: {embeddings.shape}")

# Build FAISS index
index = vector_store.build_index(embeddings)
print(f"Number of vectors in index: {index.ntotal}")

# Save vector store
vector_store.save_index(index)
print("Index saved successfully.")

vector_store.save_chunks(chunks)
print("Chunks saved successfully.")


# Create embedding for the user's question
query = "What are Mariam's technical skills?"
query_embedding = vector_store.model.encode([query])


# Load the saved vector store
loaded_index = vector_store.load_index()
loaded_chunks = vector_store.load_chunks()

print(f"Loaded index contains: {loaded_index.ntotal} vectors")
print(f"Loaded chunks: {len(loaded_chunks)}")


# Search for the most relevant chunks
distances, indices = vector_store.search_index(
    loaded_index,
    query_embedding,
    top_k=3
)


# Display retrieved chunks
print("\nRetrieved chunks:")

for rank, chunk_index in enumerate(indices[0], start=1):
    print(f"\n--- Result {rank} ---")
    print(f"Chunk index: {chunk_index}")
    print(f"Distance: {distances[0][rank - 1]}")
    print(loaded_chunks[chunk_index].page_content)