# ASSIGNMENT 10: FROM CLASS DIAGRAM TO CODE WITH ALL CREATIONAL PATTERNS

## Project Overview
This folder contains the implementation of **THE IT CODE ACADEMY** system based on the UML Class Diagram from Assignment 9.

**Language Chosen**: Python  
**Reason**: Python was selected because it is clean, readable, beginner-friendly, and ideal for an educational platform like THE IT CODE ACADEMY. It also has excellent support for design patterns and unit testing with `pytest`.

## 1. Class Implementation (`/src`)

I have successfully translated the Mermaid.js Class Diagram into working Python code.

**Classes Implemented:**
- `User` (Abstract Base Class)
- `Student` (inherits from User)
- `Instructor` (inherits from User)
- `Course`
- `Lesson` (Composition with Course)
- `Enrollment` (Association class between Student and Course)

**Key Design Decisions:**
- Used abstract base class (`ABC`) for `User` to enforce the `get_role()` method.
- Implemented business rule: Students can enroll in maximum **5 active courses**.
- Used composition for `Course` → `Lesson` relationship.
- Used properties for encapsulation (getters).

## 2. Creational Patterns Implementation (`/creational_patterns`)

All six creational design patterns have been implemented with clear, academy-relevant use cases:

| Pattern              | Use Case in THE IT CODE ACADEMY                        | Justification |
|----------------------|----------------------------------------------------------|-------------|
| **Simple Factory**   | Creating different types of learning content (Video, Quiz, Article) | Centralized and easy content creation |
| **Factory Method**   | Issuing different types of certificates (Basic vs Premium) | Allows subclasses to decide certificate type |
| **Abstract Factory** | Creating UI components for different themes (Dark/Light) | Creates families of related UI objects |
| **Builder**          | Building complex Course objects with optional features (quizzes, certificate, projects) | Handles many optional parameters cleanly |
| **Prototype**        | Cloning pre-configured Lesson templates                  | Avoids repetitive initialization |
| **Singleton**        | DatabaseConnection / NotificationService                 | Ensures only one instance exists globally |

## 3. Unit Testing

Unit tests will be added in the `/tests` directory using `pytest`. Tests cover object creation, business rules (e.g., enrollment limit), and edge cases for each pattern.

## How to Run

```bash
cd Assignment\ 10
pip install -r requirements.txt
python -m pytest tests/ -v --cov


## Design Rationale: ##  All patterns were chosen to demonstrate real-world usage in an e-learning platform while staying true to the original UML class diagram.
