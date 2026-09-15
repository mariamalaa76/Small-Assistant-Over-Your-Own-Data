from pathlib import Path

from langchain_core.documents import Document

from document_processor.loaders.pdf_loader import PDFLoader
from document_processor.loaders.txt_loader import TXTLoader
from document_processor.loaders.rtf_loader import RTFLoader


class DocumentProcessor:

    def __init__(self):
        self.loaders = {
            ".pdf": PDFLoader(),
            ".txt": TXTLoader(),
            ".rtf": RTFLoader(),
        }

    def load_documents(self, folder_path: str) -> list[Document]:
        folder = Path(folder_path)

        if not folder.exists():
            raise ValueError(f"Folder not found: {folder_path}")

        documents = []

        for file_path in folder.iterdir():

            if not file_path.is_file():
                continue

            extension = file_path.suffix.lower()

            if extension not in self.loaders:
                continue

            loader = self.loaders[extension]
            documents.extend(loader.load(str(file_path)))

        return documents