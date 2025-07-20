# AbstractProduct
class Button:
    def draw(self):
        raise NotImplementedError


class Checkbox:
    def draw(self):
        raise NotImplementedError


# ConcreteProduct
class WindowsButton(Button):
    def draw(self):
        return "Drawing a Windows Button"


class WindowsCheckbox(Checkbox):
    def draw(self):
        return "Drawing a Windows Checkbox"


class MacOSButton(Button):
    def draw(self):
        return "Drawing a MacOS Button"


class MacOSCheckbox(Checkbox):
    def draw(self):
        return "Drawing a MacOS Checkbox"


# AbstractFactory
class GUIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError


# ConcreteFactory
class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


def create_ui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button.draw(), checkbox.draw()


if __name__ == "__main__":
    windows_factory = WindowsGUIFactory()
    windows_button, windows_checkbox = create_ui(windows_factory)
    print(f"Windows UI: {windows_button}, {windows_checkbox}")

    macos_factory = MacOSGUIFactory()
    macos_button, macos_checkbox = create_ui(macos_factory)
    print(f"MacOS UI: {macos_button}, {macos_checkbox}")
