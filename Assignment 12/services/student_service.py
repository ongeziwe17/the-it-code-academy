import json
import os

class StudentService:
    """Service layer for Student business logic with persistence"""
    
    def __init__(self):
        self.file_path = "data/students.json"
        self.students = self._load_students()

    def _load_students(self):
        os.makedirs("data", exist_ok=True)
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def _save_students(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.students, f, indent=2)

    def create_student(self, student_id: int, first_name: str, last_name: str, email: str):
        if not first_name or not last_name or not email:
            raise ValueError("First name, last name and email are required fields.")
        
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
        self._save_students()
        return student

    def get_all_students(self):
        return self.students

    def get_student_by_id(self, student_id: int):
        return next((s for s in self.students if s["student_id"] == student_id), None)

    def update_student(self, student_id: int, first_name: str = None, last_name: str = None, email: str = None):
        student = self.get_student_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        if first_name: student["first_name"] = first_name
        if last_name: student["last_name"] = last_name
        if email: student["email"] = email
            
        self._save_students()
        return student

    def delete_student(self, student_id: int):
        student = self.get_student_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        self.students.remove(student)
        self._save_students()
        return f"Student {student_id} deleted successfully"