from file_system import FileSystem


class File(FileSystem):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def print(self, indent: int = 0) -> None:
        print(" " * indent + f"File: {self.name} (Size: {self.size} KB)")