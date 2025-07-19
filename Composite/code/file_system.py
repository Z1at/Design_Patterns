from abc import ABC, abstractmethod


class FileSystem(ABC):
    @abstractmethod
    def print(self, indent: int = 0) -> None:
        pass
