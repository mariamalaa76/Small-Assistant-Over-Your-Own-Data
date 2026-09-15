import asyncio

import streamlit as st

from vector_store import VectorStore
from llm_client import generate_response


# Load the vector store and stored document chunks
vector_store = VectorStore()

index = vector_store.load_index()
chunks = vector_store.load_chunks()


st.title("Small Assistant")


if prompt := st.chat_input("Ask me something..."):

    # Display user's question
    with st.chat_message("user"):
        st.write(prompt)

    # Convert the question into an embedding
    query_embedding = vector_store.model.encode([prompt])

    # Search FAISS for the most relevant chunks
    distances, indices = vector_store.search_index(
        index,
        query_embedding,
        top_k=3
    )

    # Get the actual text of the retrieved chunks
    retrieved_chunks = [
        chunks[chunk_index].page_content
        for chunk_index in indices[0]
    ]

    # Combine retrieved chunks into one context
    context = "\n\n".join(retrieved_chunks)

    # Build the prompt that will be sent to the LLM
    llm_prompt = f"""
You are a helpful assistant answering questions using the provided context.

Context:
{context}

Question:
{prompt}

Answer the question based only on the provided context.
If the answer cannot be found in the context, say:
"I don't have enough information in the provided documents."
"""

    # Generate the answer asynchronously
    response = asyncio.run(
        generate_response(llm_prompt)
    )

    # Display the final answer
    with st.chat_message("assistant"):
        st.write(response)