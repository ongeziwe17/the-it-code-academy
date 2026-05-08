# Implementing a Persistence Repository Layer

## Objective
Successfully designed and implemented a clean **Repository Layer** that abstracts storage details behind interfaces, following all assignment requirements.

## Project Structure

```bash
Assignment 11/
├── repositories/                          # Repository Interfaces
│   ├── repository.py                      # Generic Repository<T, ID>
│   ├── student_repository.py
│   ├── instructor_repository.py
│   ├── course_repository.py
│   └── enrollment_repository.py
├── repositories/inmemory/                 # In-Memory Implementations
│   ├── in_memory_student_repository.py
│   ├── in_memory_instructor_repository.py
│   ├── in_memory_course_repository.py
│   └── in_memory_enrollment_repository.py
├── repositories/database/                 # Future Storage Backends
│   └── database_course_repository.py      # Stub
├── factories/                             # Abstraction Mechanism
│   └── repository_factory.py
├── tests/                                 # Unit Tests
│   └── test_student_repository.py
└── diagrams/                              # Class Diagrams
```
---

## Design Decisions & Justification

### 1. Repository Interface Design
- Created a **generic** `Repository[T, ID]` interface with all required CRUD operations.
- Extended it with **entity-specific** repositories for better type safety and future customization.

### 2. In-Memory Implementation 
- Used Python `dict` (HashMap) for fast and simple in-memory storage.
- All CRUD operations (`save`, `find_by_id`, `find_all`, `delete`) are fully implemented.

### 3. Storage Abstraction Mechanism 
- Used **Factory Pattern** (`RepositoryFactory`) to decouple the application from specific storage implementations.
- Makes switching between in-memory, database, or filesystem very easy.

### 4. Future-Proofing 
- Added a `DatabaseCourseRepository` stub showing readiness for real database integration.
- The system is designed to easily support JSON files, SQL databases, or external APIs.

## How to Use

```python
from factories.repository_factory import RepositoryFactory
from src.student import Student
from src.course import Course

# Get repositories (in-memory by default)
student_repo = RepositoryFactory.get_student_repository()
course_repo = RepositoryFactory.get_course_repository()

# Example: Create and Save a Student
student = Student(
    student_id=101,
    first_name="Keo",
    last_name="Makhubo",
    email="keocodes@gmail.com"
    # Add other required fields as per your Student class
)

student_repo.save(student)
print("Student saved successfully!")

# Retrieve example
found = student_repo.find_by_id(101)
print(f"Found student: {found.first_name if found else None}")
```
## Why This Matters

- **Separation of Concerns**: Business logic stays independent of storage details.
- **Scalability**: Switching to a real database becomes trivial.
- **Testability**: In-memory repositories enable fast unit testing.
- **Maintainability**: Clean, extensible architecture.

## Future Enhancements

- Full SQL Database implementation (SQLAlchemy)
- JSON File-based repository
- Comprehensive unit tests with pytest

---

## Class Diagram (Updated for Repository Layer)

```mermaid
classDiagram
    class Repository~T, ID~ {
        <<interface>>
        +save(entity: T)
        +findById(id: ID) T
        +findAll() List~T~
        +delete(id: ID)
    }

    class StudentRepository
    class InstructorRepository
    class CourseRepository
    class EnrollmentRepository

    Repository <|-- StudentRepository
    Repository <|-- InstructorRepository
    Repository <|-- CourseRepository
    Repository <|-- EnrollmentRepository

    class InMemoryStudentRepository
    class InMemoryCourseRepository

    StudentRepository <|-- InMemoryStudentRepository
    CourseRepository <|-- InMemoryCourseRepository

    class RepositoryFactory
---
