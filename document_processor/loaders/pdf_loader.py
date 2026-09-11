from .base_loader import BaseLoader
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

class PDFLoader(BaseLoader):
    def load(self, file_path: str) -> list[Document]:
        path = Path(file_path)
        if not path.exists():
            raise ValueError(f"File {file_path} does not exist.")
        if path.stat().st_size == 0:
            raise ValueError(f"File {file_path} is empty.")
        if not path.is_file():
            raise ValueError(f"File {file_path} is not a valid file.")
        
        try:
            pdf_loader = PyPDFLoader(file_path)
            documents = pdf_loader.load()
            return documents
        except Exception as e:
            raise ValueError(f"Error occurred while loading PDF file {file_path}: {str(e)}")