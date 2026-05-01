import pytest
from src.user import Student, Instructor
from src.course import Course
from src.lesson import Lesson
from src.enrollment import Enrollment

def test_student_max_enrollment_limit():
    """Test business rule: Student cannot enroll in more than 5 courses"""
    instructor = Instructor(1, "Mr. Smith", "smith@academy.com")
    course = Course(101, "Python Basics", instructor)
    
    student = Student(1001, "Alice Wonder", "alice@email.com")
    
    # Enroll 5 times successfully
    for i in range(5):
        student.enroll_in_course(course)
    
    # 6th enrollment should raise error
    with pytest.raises(ValueError, match="cannot enroll in more than 5"):
        student.enroll_in_course(course)


def test_inheritance_and_roles():
    student = Student(1001, "Alice", "alice@email.com")
    instructor = Instructor(2001, "Bob", "bob@academy.com")
    
    assert student.get_role() == "Student"
    assert instructor.get_role() == "Instructor"


def test_enrollment_progress():
    instructor = Instructor(1, "Mr. Smith", "smith@academy.com")
    course = Course(101, "Python Basics", instructor)
    student = Student(1001, "Alice", "alice@email.com")
    
    enrollment = student.enroll_in_course(course)
    enrollment.update_progress(75.5)
    
    assert enrollment.progress == 75.5