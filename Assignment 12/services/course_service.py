from typing import List, Optional

class CourseService:
    def __init__(self, course_repo):
        self.course_repo = course_repo

    def create_course(self, course_id: int, title: str, description: str, instructor_id: int):
        """Create new course with validation"""
        if not title:
            raise ValueError("Course title is required")
        
        try:
            from src.course import Course
        except ImportError:
            try:
                from Assignment_9.src.course import Course
            except ImportError:
                from Assignment_11.src.course import Course
        
        course = Course(
            course_id=course_id,
            title=title,
            description=description,
            instructor_id=instructor_id
        )
        return self.course_repo.save(course)

    def get_all_courses(self):
        return self.course_repo.find_all()

    def get_course_by_id(self, course_id: int):
        return self.course_repo.find_by_id(course_id)