from typing import List, Optional, Dict
from repositories.student_repository import StudentRepository
from src.student import Student


class InMemoryStudentRepository(StudentRepository):
    """In-memory implementation using Python dictionary (HashMap)"""

    def __init__(self):
        self._storage: Dict[int, Student] = {}

    def save(self, student: Student) -> None:
        self._storage[student.student_id] = student
        print(f"✅ Student saved: {student.first_name} {student.last_name}")

    def find_by_id(self, student_id: int) -> Optional[Student]:
        return self._storage.get(student_id)

    def find_all(self) -> List[Student]:
        return list(self._storage.values())

    def delete(self, student_id: int) -> None:
        if student_id in self._storage:
            del self._storage[student_id]
            print(f"🗑️ Student deleted: ID {student_id}")