import json
from services.student_service import StudentService
from services.course_service import CourseService

def seed_data():
    student_service = StudentService()
    course_service = CourseService()

    print("Seeding data...")

    # Load Courses
    with open('courses.json', 'r') as f:
        courses = json.load(f)
    
    for c in courses:
        try:
            course_service.create_course(
                course_id=c["course_id"],
                title=c["title"],
                description=c["description"],
                instructor_id=c.get("instructor_id", 1)
            )
        except:
            pass  # skip duplicates

    # Load Students
    with open('students.json', 'r') as f:
        students = json.load(f)
    
    for s in students:
        try:
            student_service.create_student(
                student_id=s["student_id"],
                first_name=s["first_name"],
                last_name=s["last_name"],
                email=s["email"]
            )
        except:
            pass  # skip duplicates

    print(f" Seeded {len(course_service.get_all_courses())} courses and {len(student_service.get_all_students())} students")

if __name__ == "__main__":
    seed_data()