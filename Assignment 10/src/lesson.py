class Lesson:
    """Represents a Lesson inside a Course (Composition relationship)"""
    def __init__(self, lesson_id: int, title: str, content: str, course: 'Course'):
        self._lesson_id = lesson_id
        self._title = title
        self._content = content
        self._course = course
        course.add_lesson(self)   # Composition: Lesson belongs to Course

    @property
    def lesson_id(self) -> int:
        return self._lesson_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    @property
    def course(self) -> 'Course':
        return self._course