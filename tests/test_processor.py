from document_processor.processor import DocumentProcessor
processor = DocumentProcessor()
documents = processor.load_documents("data")
print(f"Total documents loaded: {len(documents)}")
for document in documents:
    print(f"- {document.metadata.get('source')}")