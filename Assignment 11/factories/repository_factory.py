from repositories.inmemory.in_memory_student_repository import InMemoryStudentRepository
from repositories.inmemory.in_memory_instructor_repository import InMemoryInstructorRepository
from repositories.inmemory.in_memory_course_repository import InMemoryCourseRepository
from repositories.inmemory.in_memory_enrollment_repository import InMemoryEnrollmentRepository


class RepositoryFactory:
    """
    Factory Pattern to create repository instances.
    This makes it very easy to switch between different storage backends
    (in-memory, database, filesystem, etc.) in the future.
    """

    @staticmethod
    def get_student_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryStudentRepository()
        # Future implementations can be added here
        # elif storage_type == "DATABASE":
        #     return DatabaseStudentRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

    @staticmethod
    def get_instructor_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryInstructorRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

    @staticmethod
    def get_course_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryCourseRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

    @staticmethod
    def get_enrollment_repository(storage_type: str = "MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryEnrollmentRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")