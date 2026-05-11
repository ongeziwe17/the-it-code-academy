from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(
    title="The IT Code Academy - REST API",
    description="Assignment 12: Service Layer + REST API",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ===================== SERVICES =====================
class StudentService:
    def __init__(self):
        self.students = []

    def create_student(self, student_id: int, first_name: str, last_name: str, email: str):
        if not first_name or not last_name or not email:
            raise ValueError("First name, last name and email are required")
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
        return self.students

class CourseService:
    def __init__(self):
        self.courses = []

    def create_course(self, course_id: int, title: str, description: str):
        if not title:
            raise ValueError("Course title is required")
        course = {
            "course_id": course_id,
            "title": title,
            "description": description
        }
        self.courses.append(course)
        return course

    def get_all_courses(self):
        return self.courses

class EnrollmentService:
    def __init__(self, student_service):
        self.student_service = student_service

    def enroll_student(self, student_id: int, course_id: int):
        student = next((s for s in self.student_service.students if s["student_id"] == student_id), None)
        if not student:
            raise ValueError(f"Student {student_id} not found")
        
        # Business Rule: Max 5 courses
        if len(student["enrolled_courses"]) >= 5:
            raise ValueError("Student cannot enroll in more than 5 courses")
        
        if course_id in student["enrolled_courses"]:
            raise ValueError("Already enrolled in this course")
        
        student["enrolled_courses"].append(course_id)
        return {"message": f"Student {student_id} enrolled in course {course_id}", 
                "student": student}

# Initialize Services
student_service = StudentService()
course_service = CourseService()
enrollment_service = EnrollmentService(student_service)

# ===================== ENDPOINTS =====================
@app.get("/")
def root():
    return {"message": "✅ Assignment 12 API is running successfully!"}

@app.get("/api/students")
def get_all_students():
    return student_service.get_all_students()

@app.post("/api/students")
def create_student(student_id: int, first_name: str, last_name: str, email: str):
    student = student_service.create_student(student_id, first_name, last_name, email)
    return {"message": "Student created successfully", "student": student}

@app.get("/api/courses")
def get_all_courses():
    return course_service.get_all_courses()

@app.post("/api/courses")
def create_course(course_id: int, title: str, description: str):
    course = course_service.create_course(course_id, title, description)
    return {"message": "Course created successfully", "course": course}

@app.post("/api/students/{student_id}/enroll")
def enroll_student(student_id: int, course_id: int):
    try:
        result = enrollment_service.enroll_student(student_id, course_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

print("🚀 Full Assignment 12 API Ready!")
print("→ http://localhost:8000/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)