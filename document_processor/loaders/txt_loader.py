from pathlib import Path
from langchain_core.documents import Document
from .base_loader import BaseLoader

class TXTLoader(BaseLoader):
    def load(self, file_path: str) -> list[Document]:
        path = Path(file_path)
        if not path.exists():
            raise ValueError(f"TXT file not found: {file_path}")
        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")
        try:
            text = path.read_text(encoding="utf-8")
            document = Document(
                page_content=text,
                metadata={"source": str(path),"file_type": "txt"})
            return [document]
        except Exception as e:
            raise ValueError(f"Failed to read TXT file '{file_path}': {e}") from e