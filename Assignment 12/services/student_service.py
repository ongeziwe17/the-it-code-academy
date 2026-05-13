class StudentService:
    """Service layer for Student business logic"""
    
    def __init__(self):
        self.students = []

    def create_student(self, student_id: int, first_name: str, last_name: str, email: str):
        """Create a new student with validation"""
        if not first_name or not last_name or not email:
            raise ValueError("First name, last name and email are required fields.")
        
        # Check if student already exists
        if any(s["student_id"] == student_id for s in self.students):
            raise ValueError(f"Student with ID {student_id} already exists.")
        
        student = {
            "student_id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "enrolled_courses": []
        }
        
        self.students.append(student)
        return student

    def get_all_students(self):
        """Return all students"""
        return self.students

    def get_student_by_id(self, student_id: int):
        """Find student by ID"""
        return next((s for s in self.students if s["student_id"] == student_id), None)