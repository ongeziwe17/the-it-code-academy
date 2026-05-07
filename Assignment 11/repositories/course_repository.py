from repositories.repository import Repository
from src.course import Course


class CourseRepository(Repository[Course, int]):
    """Course-specific repository interface"""
    pass