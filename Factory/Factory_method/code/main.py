# Product
class Document:
    def __init__(self, content):
        self.content = content

    def render(self):
        raise NotImplementedError("Subclasses must implement this method")


# ConcreteProduct
class PDFDocument(Document):
    def render(self):
        return f"Rendering PDF Document: {self.content}"


class HTMLDocument(Document):
    def render(self):
        return f"Rendering HTML Document: {self.content}"


# Creator
class DocumentCreator:
    def create_document(self, content):
        raise NotImplementedError("Subclasses must implement this method")

    def display_document(self, content):
        document = self.create_document(content)
        print(document.render())


# ConcreteCreator
class PDFDocumentCreator(DocumentCreator):
    def create_document(self, content):
        return PDFDocument(content)


class HTMLDocumentCreator(DocumentCreator):
    def create_document(self, content):
        return HTMLDocument(content)


if __name__ == "__main__":
    pdf_creator = PDFDocumentCreator()
    pdf_creator.display_document("This is a PDF document")

    html_creator = HTMLDocumentCreator()
    html_creator.display_document("This is an HTML document")
