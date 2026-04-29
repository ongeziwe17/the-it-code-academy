from abc import ABC, abstractmethod

class Content(ABC):
    """Base class for different types of learning content"""
    @abstractmethod
    def display(self):
        pass

class VideoContent(Content):
    def display(self):
        return "🎥 Playing video lesson..."

class QuizContent(Content):
    def display(self):
        return "📝 Starting interactive quiz..."

class ArticleContent(Content):
    def display(self):
        return "📖 Opening reading material..."

class ContentFactory:
    """Simple Factory - Centralized object creation"""
    @staticmethod
    def create_content(content_type: str) -> Content:
        if content_type.lower() == "video":
            return VideoContent()
        elif content_type.lower() == "quiz":
            return QuizContent()
        elif content_type.lower() == "article":
            return ArticleContent()
        else:
            raise ValueError(f"Unknown content type: {content_type}")