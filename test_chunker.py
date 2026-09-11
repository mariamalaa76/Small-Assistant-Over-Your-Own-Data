from document_processor.loaders.pdf_loader import PDFLoader
from document_processor.loaders.txt_loader import TXTLoader
from document_processor.loaders.rtf_loader import RTFLoader
from document_processor.chunker import DocumentChunker


def main():
    chunker = DocumentChunker()
    files = [
        ("PDF", PDFLoader(), "data/Mariam_Abdelfattah_CV 3.pdf"),
        ("TXT", TXTLoader(), "data/AI Engineer job_1.txt"),
        ("RTF", RTFLoader(), "data/Study Notes.rtf"),
        ]

    for file_type, loader, file_path in files:
        documents = loader.load(file_path)
        chunks = chunker.chunk_documents(documents)
        print(f"\n{file_type}")
        print(f"Documents: {len(documents)}")
        print(f"Chunks: {len(chunks)}")


if __name__ == "__main__":
    main()