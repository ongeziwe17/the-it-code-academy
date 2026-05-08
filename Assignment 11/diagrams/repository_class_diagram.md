\# Repository Layer Class Diagram



```mermaid

classDiagram

&#x20;   class Repository\~T, ID\~ {

&#x20;       <<interface>>

&#x20;       +save(T entity)

&#x20;       +findById(ID id) T

&#x20;       +findAll() List\~T\~

&#x20;       +delete(ID id)

&#x20;   }



&#x20;   class StudentRepository

&#x20;   class InstructorRepository

&#x20;   class CourseRepository

&#x20;   class EnrollmentRepository



&#x20;   Repository <|-- StudentRepository

&#x20;   Repository <|-- InstructorRepository

&#x20;   Repository <|-- CourseRepository

&#x20;   Repository <|-- EnrollmentRepository



&#x20;   class InMemoryStudentRepository

&#x20;   class InMemoryInstructorRepository

&#x20;   class InMemoryCourseRepository

&#x20;   class InMemoryEnrollmentRepository



&#x20;   StudentRepository <|-- InMemoryStudentRepository

&#x20;   InstructorRepository <|-- InMemoryInstructorRepository

&#x20;   CourseRepository <|-- InMemoryCourseRepository

&#x20;   EnrollmentRepository <|-- InMemoryEnrollmentRepository



&#x20;   class RepositoryFactory

