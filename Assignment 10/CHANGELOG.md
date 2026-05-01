# Changelog - Assignment 10

### Added
- Core domain classes in `src/` (User, Student, Instructor, Course, Lesson, Enrollment)
- All six creational design patterns in `creational_patterns/` with academy-relevant examples
- Comprehensive unit tests in `tests/` for core classes and all patterns
- Business rule enforcement (max 5 courses per student)
- Strong documentation in README.md with design decisions and pattern justifications

### Implemented Creational Patterns
- **Simple Factory**: Content creation (Video, Quiz, Article)
- **Factory Method**: Certificate issuance (Basic vs Premium)
- **Abstract Factory**: UI Theme components (Dark/Light)
- **Builder**: Flexible Course construction with optional features
- **Prototype**: Lesson template cloning
- **Singleton**: DatabaseConnection

### Testing
- Unit tests for class relationships, inheritance, and business rules
- Tests for all six creational patterns (object creation, edge cases, singleton behavior)
- Ready for coverage report using `pytest-cov`

## [2026-04-30] - Initial Implementation
- Translated UML Class Diagram into Python source code
- Set up project structure inside `Assignment 10/`

---
