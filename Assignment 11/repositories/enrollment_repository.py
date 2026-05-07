from repositories.repository import Repository
from src.enrollment import Enrollment


class EnrollmentRepository(Repository[Enrollment, int]):
    """Enrollment-specific repository interface"""
    pass