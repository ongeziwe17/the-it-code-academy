# Implementing a Persistence Repository Layer

## Objective
Successfully designed and implemented a clean **Repository Layer** that abstracts storage details behind interfaces, following all assignment requirements.

## Project Structure
```
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
├── repositories/database/                 # Future-Proof Stub
│   └── database_course_repository.py
├── factories/                             # Storage Abstraction
│   └── repository_factory.py
├── tests/                                 # Unit Tests (to be added)
└── diagrams/                              # Class Diagram
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

# Get repository
student_repo = RepositoryFactory.get_student_repository()

# Example CRUD operations
student = Student(student_id=1, first_name="John", last_name="Doe", ...)
student_repo.save(student)

found = student_repo.find_by_id(1)
all_students = student_repo.find_all()
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
