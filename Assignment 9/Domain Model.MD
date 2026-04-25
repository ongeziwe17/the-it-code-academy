# DOMAIN MODEL

After reviewing the system requirements (Assignment 4), use cases (Assignment 5), Agile planning (Assignment 6), and behavioral models (Assignment 8), I identified the following six core domain entities for THE IT CODE ACADEMY.

### Key Domain Entities

| Entity          | Attributes                                                                 | Methods / Responsibilities                                      | Relationships |
|-----------------|----------------------------------------------------------------------------|------------------------------------------------------------------|---------------|
| **User**       | userId: String, name: String, email: String, passwordHash: String, role: Enum (Student, Instructor, Admin), dateJoined: Date | register(), login(), logout(), updateProfile(), viewProgress() | Enrolls in Courses through Enrollment; Takes Assessments; Can be Student or Instructor |
| **Student**    | (inherits from User) + learningGoals: List~String~                        | enrollInCourse(), markLessonComplete(), viewMyCourses()         | Inherits from User; Has many Enrollments |
| **Instructor** | (inherits from User) + bio: String, expertiseAreas: List~String~, yearsOfExperience: Integer | createCourse(), addLesson(), reviewAssessmentSubmission(), publishCourse() | Inherits from User; Teaches many Courses |
| **Course**     | courseId: String, title: String, description: String, difficultyLevel: Enum (Beginner, Intermediate, Advanced), durationInHours: Integer, isFree: Boolean, category: String | addLesson(), publish(), calculateAverageCompletionRate(), getLessons() | Contains many Lessons; Has many Assessments; Taught by one Instructor |
| **Lesson**     | lessonId: String, title: String, content: Text, videoUrl: String, durationInMinutes: Integer, orderNumber: Integer | markAsCompleted(user: User), getNextLesson()                    | Belongs to one Course; May have Quizzes |
| **Assessment** | assessmentId: String, title: String, type: Enum (Quiz, Project, FinalExam), passingScore: Integer, totalPoints: Integer | submitAnswers(answers: List), calculateScore(), generateFeedback() | Belongs to one Course; Taken by many Students |
| **Enrollment** | enrollmentId: String, enrollmentDate: Date, completionPercentage: Float (0-100), status: Enum (Active, Completed, Dropped), lastAccessed: Date | updateProgress(percentage: Float), issueCertificate(), checkCompletion() | Associates one Student with one Course; Tracks individual progress |

### Business Rules
- A Student can have a maximum of **5 active Enrollments** at any time.
- Only Instructors and Admins can create, modify, or publish Courses and Lessons.
- Assessments require a minimum passing score of **70%**.
- Certificates are issued only when an Enrollment reaches 100% completion and all required Assessments are passed.
- Progress updates automatically when Lessons are completed or Assessments are submitted.
- Instructors are notified when Students submit Assessments for review.

This domain model captures the essential business logic needed to deliver structured, trackable programming education to underserved youth.


