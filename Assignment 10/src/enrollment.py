from datetime import datetime

class Enrollment:
    """Association class between Student and Course"""
    def __init__(self, student: 'Student', course: 'Course'):
        self._student = student
        self._course = course
        self._enrollment_date = datetime.now()
        self._progress = 0.0  # Progress percentage

    @property
    def student(self) -> 'Student':
        return self._student

    @property
    def course(self) -> 'Course':
        return self._course

    @property
    def enrollment_date(self):
        return self._enrollment_date

    @property
    def progress(self) -> float:
        return self._progress

    def update_progress(self, new_progress: float):
        """Update student's progress in the course"""
        if 0 <= new_progress <= 100:
            self._progress = new_progress
            print(f"Progress updated to {new_progress}% for {self.student.name} in {self.course.title}")
        else:
            raise ValueError("Progress must be between 0 and 100.")