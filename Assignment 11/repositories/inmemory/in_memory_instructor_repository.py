from typing import List, Optional, Dict
from repositories.instructor_repository import InstructorRepository
from src.instructor import Instructor


class InMemoryInstructorRepository(InstructorRepository):
    """In-memory implementation for Instructor"""

    def __init__(self):
        self._storage: Dict[int, Instructor] = {}

    def save(self, instructor: Instructor) -> None:
        self._storage[instructor.instructor_id] = instructor
        print(f"✅ Instructor saved: {instructor.first_name} {instructor.last_name}")

    def find_by_id(self, instructor_id: int) -> Optional[Instructor]:
        return self._storage.get(instructor_id)

    def find_all(self) -> List[Instructor]:
        return list(self._storage.values())

    def delete(self, instructor_id: int) -> None:
        if instructor_id in self._storage:
            del self._storage[instructor_id]
            print(f"🗑️ Instructor deleted: ID {instructor_id}")