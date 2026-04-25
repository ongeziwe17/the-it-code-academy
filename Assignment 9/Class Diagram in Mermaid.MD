# CLASS DIAGRAM IN MERMAID.js

```mermaid
classDiagram
    class User {
        -userId: String
        -name: String
        -email: String
        -passwordHash: String
        -role: RoleEnum
        -dateJoined: Date
        +register()
        +login()
        +logout()
        +updateProfile()
        +viewProgress()
    }

    class Student {
        -learningGoals: List
        +enrollInCourse(course: Course)
        +markLessonComplete(lesson: Lesson)
        +viewMyCourses()
    }

    class Instructor {
        -bio: String
        -expertiseAreas: List
        -yearsOfExperience: Integer
        +createCourse()
        +addLesson(course: Course, lesson: Lesson)
        +reviewAssessmentSubmission()
        +publishCourse(course: Course)
    }

    class Course {
        -courseId: String
        -title: String
        -description: String
        -difficultyLevel: DifficultyEnum
        -durationInHours: Integer
        -isFree: Boolean
        -category: String
        +addLesson(lesson: Lesson)
        +publish()
        +calculateAverageCompletionRate()
    }

    class Lesson {
        -lessonId: String
        -title: String
        -content: String
        -videoUrl: String
        -durationInMinutes: Integer
        -orderNumber: Integer
        +markAsCompleted(user: User)
        +getNextLesson()
    }

    class Assessment {
        -assessmentId: String
        -title: String
        -type: AssessmentTypeEnum
        -passingScore: Integer
        -totalPoints: Integer
        +submitAnswers(answers: List, student: Student)
        +calculateScore()
        +generateFeedback()
    }

    class Enrollment {
        -enrollmentId: String
        -enrollmentDate: Date
        -completionPercentage: Float
        -status: EnrollmentStatusEnum
        -lastAccessed: Date
        +updateProgress(percentage: Float)
        +issueCertificate()
        +checkCompletion()
    }

    User <|-- Student
    User <|-- Instructor

    Student "1" -- "0..5" Enrollment : has
    Enrollment "1" --> "1" Course : for
    Course "1" *-- "1..*" Lesson : contains
    Course "1" o-- "0..*" Assessment : includes
    Instructor "1" -- "0..*" Course : teaches
    Student "1" -- "0..*" Assessment : takes
