from repositories.repository import Repository
from src.student import Student


class StudentRepository(Repository[Student, int]):
    """Student-specific repository interface"""
    pass