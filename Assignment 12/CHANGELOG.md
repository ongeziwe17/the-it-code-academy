# CHANGELOG

### Added
- Full Service Layer (`StudentService`, `CourseService`, `EnrollmentService`)
- REST API with **Full CRUD** operations using FastAPI
- Business Rule: Students cannot enroll in more than 5 courses
- JSON-based data persistence (data survives server restarts)
- Seed data support (`seed_data.py`, `students.json`, `courses.json`)
- Comprehensive error handling and input validation

### Features
- Interactive Swagger UI documentation
- Persistent storage in `data/` folder
- Clean layered architecture (Service → API)

### Screenshots
- Full Swagger UI
- Create Student/Course
- Enrollment business rule enforcement



