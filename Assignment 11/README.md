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
