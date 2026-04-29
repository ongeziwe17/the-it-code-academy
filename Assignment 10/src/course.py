from typing import List

class Course:
    """Represents a Course in The IT Code Academy"""
    def __init__(self, course_id: int, title: str, instructor: 'Instructor'):
        self._course_id = course_id
        self._title = title
        self._instructor = instructor
        self._lessons: List['Lesson'] = []
        instructor.add_course(self)   # Association with Instructor

    @property
    def course_id(self) -> int:
        return self._course_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def instructor(self) -> 'Instructor':
        return self._instructor

    @property
    def lessons(self) -> List['Lesson']:
        return self._lessons

    def add_lesson(self, lesson: 'Lesson'):
        self._lessons.append(lesson)