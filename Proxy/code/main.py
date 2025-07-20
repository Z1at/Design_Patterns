"""
Виртуальный прокси, отложенная загрузка изображения
"""


class Image:
    def __init__(self, filename):
        self.filename = filename
        self.image = None  # Изображение еще не загружено

    def display(self):
        raise NotImplementedError


class RealImage(Image):
    def __init__(self, filename):
        super().__init__(filename)
        self.load_from_disk()  # Загрузка сразу при создании

    def load_from_disk(self):
        print(f"Loading {self.filename} from disk...")
        self.image = f"Image data for {self.filename}"
        print(f"Image {self.filename} loaded.")

    def display(self):
        print(f"Displaying {self.image}")


class ProxyImage(Image):
    def __init__(self, filename):
        super().__init__(filename)
        self.real_image = None  # Реальное изображение еще не создано

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)  # Загружаем только при необходимости
        self.real_image.display()


if __name__ == "__main__":
    image1 = ProxyImage("image1.jpg")
    image2 = ProxyImage("image2.png")

    print("Images created (not loaded yet).")

    image1.display()  # Вот тут произойдет загрузка image1
    image2.display()  # Вот тут произойдет загрузка image2
