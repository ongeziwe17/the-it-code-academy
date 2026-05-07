from repositories.repository import Repository
from src.instructor import Instructor


class InstructorRepository(Repository[Instructor, int]):
    """Instructor-specific repository interface"""
    pass