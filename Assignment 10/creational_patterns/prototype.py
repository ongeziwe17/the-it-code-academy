import copy
from abc import ABC, abstractmethod

class LessonPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class LessonTemplate(LessonPrototype):
    """Prototype Pattern - clone pre-configured lesson templates"""
    def __init__(self, title: str, content: str, difficulty: str = "Beginner"):
        self.title = title
        self.content = content
        self.difficulty = difficulty

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Lesson: {self.title} | Difficulty: {self.difficulty}"