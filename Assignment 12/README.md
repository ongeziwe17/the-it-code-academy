# SERVICE LAYER AND REST API IMPLEMENTATION

## Overview
This project implements a clean **Service Layer** that encapsulates business logic on top of the repository pattern. The services are exposed through a modern **REST API** built with **FastAPI**, complete with automatic OpenAPI/Swagger documentation and JSON persistence.

**Entities Covered**: Student, Course, and Enrollment (exceeding the minimum requirement of 3 entities).

## Features Implemented
- **Full CRUD** operations for Students and Courses
- **Business Logic**: Students cannot enroll in more than **5 courses**
- **Persistent Storage**: Data is saved in JSON files (`data/` folder) and survives server restarts
- **Input Validation** and comprehensive error handling
- **Interactive API Documentation** via Swagger UI

## Project Structure
```bash
Assignment 12/
├── main.py                     # FastAPI application entry point
├── services/
│   ├── student_service.py
│   ├── course_service.py
│   └── enrollment_service.py
├── data/                       # JSON persistence files
├── screenshots/                # Evidence for submission
├── README.md
├── CHANGELOG.md
├── seed_data.py
├── courses.json
├── students.json
└── requirements.txt

## How to Run
```bash
cd "Assignment 12"
py main.py
Access Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
```
## Technologies

- FastAPI + Uvicorn
- Python Service Layer Architecture
- JSON File-based Persistence
- Pydantic-style validation

## Deliverables Completed

- Service Layer with business logic (/services/)
- RESTful API with Full CRUD + Enrollment workflow
- Auto-generated OpenAPI/Swagger documentation
- Screenshots in /screenshots/ folder
- Data persistence and seed data
- CHANGELOG.md

## Screenshots

All required screenshots are available in the screenshots/ folder:

- [Swagger UI](./SPECIFICATION.md)
- [GET Students & Courses](./SPECIFICATION.md)
- [Enrollment business rule enforcement](./SPECIFICATION.md)
- [Project folder structure](./SPECIFICATION.md)

## GitHub Activity

- Proper commit history with meaningful messages
- Project board updated (if applicable)

  ## This submission follows industry best practices for layered architecture (Repository → Service → API).
