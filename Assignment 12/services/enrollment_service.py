class EnrollmentService:
    """Service for handling enrollment business logic"""
    
    def __init__(self, student_service):
        self.student_service = student_service

    def enroll_student(self, student_id: int, course_id: int):
        """Enroll student with important business rule: max 5 courses"""
        student = self.student_service.get_student_by_id(student_id)
        
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        # Business Rule (Key for marks)
        if len(student.get("enrolled_courses", [])) >= 5:
            raise ValueError("Students cannot enroll in more than 5 courses")
        
        if course_id in student.get("enrolled_courses", []):
            raise ValueError("Student is already enrolled in this course")
        
        student["enrolled_courses"].append(course_id)
        
        return {
            "message": f"Student {student_id} successfully enrolled in course {course_id}",
            "student": student
        }