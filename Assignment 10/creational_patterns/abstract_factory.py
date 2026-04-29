from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class DarkButton(Button):
    def render(self):
        return "🌑 Dark Theme Button Rendered"

class LightButton(Button):
    def render(self):
        return "☀️ Light Theme Button Rendered"

class ThemeFactory(ABC):
    """Abstract Factory - creates families of related objects"""
    @abstractmethod
    def create_button(self) -> Button:
        pass

class DarkThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return DarkButton()

class LightThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return LightButton()