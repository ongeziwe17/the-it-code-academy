# OBJECT STATE MODELING WITH STATE TRANSITION DIAGRAMS

## 1. User Account State Transition Diagram
![User Account State Transition Diagram](Object-State-Modeling%20Screenshots/user-account.png)

**Detailed Explanation**  
* **Key States**: Unregistered, PendingVerification, Active, Suspended, Deactivated.  
* **Key Transitions & Events**: Registration with guard (email unique), email verification, admin suspension/reactivation, user deactivation.  
* **How it maps to requirements**: Directly models the full lifecycle in **FR-001** (Create User Account & Authenticate User) and **UC: Create User Account**. Supports **US-001** from AGILE-PLANNING.md by ensuring secure onboarding for students in underserved communities. The PendingVerification state prevents fake accounts.

## 2. Course State Transition Diagram
![Course State Transition Diagram](Object-State-Modeling%20Screenshots/course.png)

**Detailed Explanation**  
* **Key States**: Draft, Published, Archived.  
* **Key Transitions & Events**: Publish only when content is complete (guard condition), archive, republish, or delete.  
* **How it maps to requirements**: Matches **FR-002** (Course Management – create, publish, browse) and **UC: Create Course**. Supports **US-006** so instructors can control when courses go live, giving students reliable, high-quality content.

## 3. Enrollment State Transition Diagram
![Enrollment State Transition Diagram](Object-State-Modeling%20Screenshots/enrollment.png)

**Detailed Explanation**  
* **Key States**: Pending, Active, Completed, Dropped.  
* **Key Transitions & Events**: Confirmation after authentication, course completion, or drop.  
* **How it maps to requirements**: Tracks the Enrollment object per **FR-002** (Enroll in course) and **UC: Enrol Course**. Links directly to **US-004** and enables progress tracking for certifications.

## 4. Quiz State Transition Diagram
![Quiz State Transition Diagram](Object-State-Modeling%20Screenshots/quiz.png)

**Detailed Explanation**  
* **Key States**: Draft, Published, Archived.  
* **Key Transitions & Events**: Publish after review (guard condition), archive.  
* **How it maps to requirements**: Supports instructor-side quiz management in **FR-003** (Quiz Management) and **UC: Create Quiz**. Aligns with **US-007**.

## 5. Quiz Attempt State Transition Diagram
![Quiz Attempt State Transition Diagram](Object-State-Modeling%20Screenshots/attempt-quiz.png)

**Detailed Explanation**  
* **Key States**: NotStarted, InProgress, Submitted, Graded, Passed, Failed.  
* **Key Transitions & Events**: Start quiz, submit (with time guard), auto-grade, outcome based on pass mark.  
* **How it maps to requirements**: Student-facing assessment flow from **FR-003** (Attempt quizzes, automatic grading) and **UC: Take Quiz**. Perfectly matches **US-008**.

## 6. Payment State Transition Diagram
![Payment State Transition Diagram](Object-State-Modeling%20Screenshots/payment.png)

**Detailed Explanation**  
* **Key States**: Initiated, Pending, Successful, Failed, Refunded.  
* **Key Transitions & Events**: Gateway calls, success/fail, retry, and refund.  
* **How it maps to requirements**: Full payment lifecycle in **FR-005** (Certification and Payments) and **UC: Process Payment**. Supports **US-010** with secure third-party integration.

## 7. Certification State Transition Diagram
![Certification State Transition Diagram](Object-State-Modeling%20Screenshots/certification.png)

**Detailed Explanation**  
* **Key States**: Requested, Awarded, Expired.  
* **Key Transitions & Events**: Awarded only when both payment and course are complete (guard condition).  
* **How it maps to requirements**: Ties directly to **FR-005** and **US-010**. Prevents invalid certifications.

## 8. Notification State Transition Diagram
![Notification State Transition Diagram](Object-State-Modeling%20Screenshots/notification.png)

**Detailed Explanation**  
* **Key States**: Queued, Sent, Failed.  
* **Key Transitions & Events**: Send attempt with retry logic (max 3 attempts).  
* **How it maps to requirements**: Supports **FR-006** (Notification System) and **US-011** for reliable student/instructor updates.
