# ASSIGNMENT 10: FROM CLASS DIAGRAMS TO CODE WITH ALL CREATIONAL PATTERNS

## Overview
This folder contains the complete implementation of **THE IT CODE ACADEMY** system, translated from the UML Class Diagram (Assignment 9) into working Python code, along with all six creational design patterns and comprehensive unit tests.

**Language Chosen**: Python 3  
**Reason for choosing Python**: Python was selected for its readability, simplicity, and suitability for an educational platform aimed at teaching programming to beginners. It also provides excellent support for design patterns and testing with `pytest`.

## 1. Class Implementation (`/src`)

I have faithfully translated the Mermaid.js Class Diagram into clean, object-oriented Python code.

**Implemented Classes:**
- `User` (Abstract Base Class)
- `Student` (inherits from `User`)
- `Instructor` (inherits from `User`)
- `Course`
- `Lesson` (Composition relationship with Course)
- `Enrollment` (Association class between Student and Course)

**Key Design Decisions:**
- Used `ABC` (Abstract Base Class) to enforce `get_role()` method.
- Encapsulation using private attributes with `@property` getters.
- Enforced business rule: A student cannot enroll in more than **5 active courses**.
- Proper implementation of inheritance, composition, and association relationships.

## 2. Creational Patterns (`/creational_patterns`)

All six major creational design patterns have been implemented with clear, context-relevant examples for an e-learning platform:

| Pattern              | Implementation Example                          | Justification |
|----------------------|--------------------------------------------------|-------------|
| **Simple Factory**   | ContentFactory (Video, Quiz, Article)           | Centralized creation of different learning content types |
| **Factory Method**   | CertificateFactory (Basic vs Premium)           | Allows subclasses to decide which certificate type to create |
| **Abstract Factory** | ThemeFactory (DarkTheme vs LightTheme)          | Creates families of related UI components |
| **Builder**          | CourseBuilder (with optional quizzes, certificate, projects) | Handles complex objects with many optional parameters cleanly |
| **Prototype**        | LessonTemplate cloning                          | Efficiently creates similar lessons without repetitive initialization |
| **Singleton**        | DatabaseConnection                              | Ensures only one database connection exists globally |

## 3. Unit Testing (`/tests`)

- **9 unit tests** written covering core classes and all creational patterns.
- Tests verify correct object creation, business rules, inheritance, and edge cases.
- **Test Coverage: 86%**

Tests include:
- Student enrollment limit enforcement
- Inheritance and role behavior
- Progress tracking in Enrollment
- Individual tests for each of the 6 creational patterns

## How to Run

```bash
cd C:\Users\keoma\the-it-code-academy\Assignment 10
pip install -r requirements.txt
py -m pytest tests/ -v --cov=src --cov=creational_patterns
```
## Project Structure

```
Assignment 10/
├── src/                    # Core domain classes
├── creational_patterns/    # All 6 creational patterns
├── tests/                  # Unit tests
├── screenshots/            # Test results and coverage report
├── README.md
├── CHANGELOG.md
└── requirements.txt
