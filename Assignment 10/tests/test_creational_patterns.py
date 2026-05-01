import pytest
from creational_patterns.simple_factory import ContentFactory
from creational_patterns.factory_method import BasicAcademyFactory, PremiumAcademyFactory
from creational_patterns.abstract_factory import DarkThemeFactory, LightThemeFactory
from creational_patterns.builder import CourseBuilder
from creational_patterns.prototype import LessonTemplate
from creational_patterns.singleton import DatabaseConnection
from src.user import Instructor

def test_simple_factory():
    video = ContentFactory.create_content("video")
    quiz = ContentFactory.create_content("quiz")
    assert "video lesson" in video.display()
    assert "quiz" in quiz.display()


def test_factory_method():
    basic_factory = BasicAcademyFactory()
    premium_factory = PremiumAcademyFactory()
    
    cert1 = basic_factory.create_certificate()
    cert2 = premium_factory.create_certificate()
    
    assert "Basic Certificate" in cert1.issue("Alice")
    assert "Premium Certificate" in cert2.issue("Alice")


def test_abstract_factory():
    dark_factory = DarkThemeFactory()
    light_factory = LightThemeFactory()
    
    assert "Dark" in dark_factory.create_button().render()
    assert "Light" in light_factory.create_button().render()


def test_builder():
    instructor = Instructor(1, "Mr. Smith", "smith@academy.com")
    course = CourseBuilder(101, "Advanced Python", instructor)\
        .add_quizzes()\
        .add_certificate()\
        .add_projects()\
        .build()
    
    assert "Advanced Python" in course


def test_prototype():
    original = LessonTemplate("Introduction to Loops", "Learn for and while loops", "Beginner")
    clone = original.clone()
    
    assert clone.title == original.title
    assert clone is not original  # Different objects


def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2  # Same instance