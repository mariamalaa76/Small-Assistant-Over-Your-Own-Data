from pathlib import Path
from langchain_core.documents import Document
from striprtf.striprtf import rtf_to_text
from .base_loader import BaseLoader

class RTFLoader(BaseLoader):
    def load(self, file_path: str) -> list[Document]:
        path = Path(file_path)
        if not path.exists():
            raise ValueError(f"RTF file not found: {file_path}")
        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")
        try:
            rtf_content = path.read_text(encoding="utf-8")
            text = rtf_to_text(rtf_content)
            document = Document(
                page_content=text,
                metadata={"source": str(path),"file_type": "rtf"})
            return [document]
        except Exception as e:
            raise ValueError(f"Failed to read RTF file '{file_path}': {e}") from e