from abc import ABC, abstractmethod
from typing import List

class User(ABC):
    """Abstract base class for all users in The IT Code Academy"""
    def __init__(self, user_id: int, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @abstractmethod
    def get_role(self) -> str:
        pass


class Student(User):
    """Student class - inherits from User"""
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self._enrollments: List['Enrollment'] = []

    def get_role(self) -> str:
        return "Student"

    def enroll_in_course(self, course: 'Course') -> 'Enrollment':
        """Enroll student in a course with a maximum limit of 5 active courses"""
        if len(self._enrollments) >= 5:
            raise ValueError(f"Student {self.name} cannot enroll in more than 5 active courses.")
        
        enrollment = Enrollment(self, course)
        self._enrollments.append(enrollment)
        print(f"✅ {self.name} successfully enrolled in {course.title}")
        return enrollment

    def get_enrollments(self):
        return self._enrollments


class Instructor(User):
    """Instructor class - inherits from User"""
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self._courses_taught: List['Course'] = []

    def get_role(self) -> str:
        return "Instructor"

    def add_course(self, course: 'Course'):
        self._courses_taught.append(course)