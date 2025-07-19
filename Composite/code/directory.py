from file_system import FileSystem


class Directory(FileSystem):
    def __init__(self, name: str):
        self.name = name
        self.contents: list = []

    def print(self, indent: int = 0) -> None:
        print(" " * indent + f"Directory: {self.name}")
        for entity in self.contents:
            entity.print(indent + 2)

    def add_entity(self, entity: FileSystem) -> None:
        self.contents.append(entity)

    def remove_entity(self, entity: FileSystem) -> None:
        if entity in self.contents:
            self.contents.remove(entity)