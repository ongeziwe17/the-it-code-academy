# Assignment 12: Service Layer and REST API Implementation

## Project Overview
Implemented a clean **Service Layer** that encapsulates business logic on top of repositories. 
Exposed via a modern **REST API** using **FastAPI** with automatic Swagger documentation.

**Entities Covered**: Student, Course, Enrollment (exceeds minimum of 3 entities).

## Key Features
- **Service Layer** (`/services/`):
  - `StudentService`
  - `CourseService` 
  - `EnrollmentService`
- **Business Logic Enforced**:
  - Students cannot enroll in more than **5 courses** (core requirement)
  - Input validation
- **REST API Endpoints**:
  - CRUD operations for Students and Courses
  - Business workflow: `/api/students/{id}/enroll`

## How to Run
```bash
cd "Assignment 12"
py main.py
Access Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
```
## Technologies

- FastAPI + Uvicorn
- Python Service Layer Architecture
- In-memory storage (structured to easily integrate with Assignment 11 repositories)

## Deliverables Completed

- Service classes in `/services/` directory (`StudentService`, `CourseService`, `EnrollmentService`)
- RESTful API endpoints with business logic
- Auto-generated OpenAPI/Swagger documentation
- Screenshots of Swagger UI and API testing in `/screenshots/`
- `CHANGELOG.md`

## Project Structure

```bash
Assignment 12/
├── main.py
├── services/
│   ├── student_service.py
│   ├── course_service.py
│   └── enrollment_service.py
├── api/ (optional)
├── tests/
├── docs/
├── screenshots/
├── README.md
└── CHANGELOG.md
