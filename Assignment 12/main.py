from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="The IT Code Academy - REST API",
    description="Assignment 12: Service Layer + REST API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import Services
from services.student_service import StudentService
from services.course_service import CourseService
from services.enrollment_service import EnrollmentService

# Initialize Services
student_service = StudentService()

# For CourseService - using simple in-memory to avoid import errors for now
class SimpleCourseRepo:
    def __init__(self):
        self.courses = []
    def save(self, course): 
        self.courses.append(course)
        return course
    def find_all(self): 
        return self.courses

course_repo = SimpleCourseRepo()
course_service = CourseService(course_repo)   # This might still cause issues if Course class is missing
enrollment_service = EnrollmentService(student_service)

@app.get("/")
def root():
    return {"message": "Assignment 12 API Running"}

@app.get("/api/students")
def get_all_students():
    return student_service.get_all_students()

@app.post("/api/students")
def create_student(student_id: int, first_name: str, last_name: str, email: str):
    try:
        student = student_service.create_student(student_id, first_name, last_name, email)
        return {"message": "Student created successfully", "student": student}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@app.get("/api/courses")
def get_all_courses():
    return course_service.get_all_courses()

@app.post("/api/courses")
def create_course(course_id: int, title: str, description: str, instructor_id: int = 1):
    try:
        course = course_service.create_course(course_id, title, description, instructor_id)
        return {"message": "Course created successfully", "course": course}
    except Exception as e:
        raise HTTPException(400, detail=str(e))

@app.post("/api/students/{student_id}/enroll")
def enroll_student(student_id: int, course_id: int):
    try:
        result = enrollment_service.enroll_student(student_id, course_id)
        return result
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

print("Server ready at http://localhost:8000/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)