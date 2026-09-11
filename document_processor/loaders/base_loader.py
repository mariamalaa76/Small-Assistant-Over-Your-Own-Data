from abc import ABC, abstractmethod
from langchain_core.documents import Document
class BaseLoader(ABC):
    @abstractmethod
    def load(self, file_path:str) -> list[Document]:
        pass