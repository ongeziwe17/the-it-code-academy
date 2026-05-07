from typing import List, Optional, Dict
from repositories.course_repository import CourseRepository
from src.course import Course


class InMemoryCourseRepository(CourseRepository):
    """In-memory implementation for Course"""

    def __init__(self):
        self._storage: Dict[int, Course] = {}

    def save(self, course: Course) -> None:
        self._storage[course.course_id] = course
        print(f"✅ Course saved: {course.title} (ID: {course.course_id})")

    def find_by_id(self, course_id: int) -> Optional[Course]:
        return self._storage.get(course_id)

    def find_all(self) -> List[Course]:
        return list(self._storage.values())

    def delete(self, course_id: int) -> None:
        if course_id in self._storage:
            del self._storage[course_id]
            print(f"🗑️ Course deleted: ID {course_id}")