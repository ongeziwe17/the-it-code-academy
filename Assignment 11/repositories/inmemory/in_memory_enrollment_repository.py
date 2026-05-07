from typing import List, Optional, Dict
from repositories.enrollment_repository import EnrollmentRepository
from src.enrollment import Enrollment


class InMemoryEnrollmentRepository(EnrollmentRepository):
    """In-memory implementation for Enrollment"""

    def __init__(self):
        self._storage: Dict[int, Enrollment] = {}

    def save(self, enrollment: Enrollment) -> None:
        self._storage[enrollment.enrollment_id] = enrollment
        print(f"✅ Enrollment saved: Student {enrollment.student_id} -> Course {enrollment.course_id}")

    def find_by_id(self, enrollment_id: int) -> Optional[Enrollment]:
        return self._storage.get(enrollment_id)

    def find_all(self) -> List[Enrollment]:
        return list(self._storage.values())

    def delete(self, enrollment_id: int) -> None:
        if enrollment_id in self._storage:
            del self._storage[enrollment_id]
            print(f"🗑️ Enrollment deleted: ID {enrollment_id}")