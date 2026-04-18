# OBJECT STATE MODELING WITH STATE TRANSITION DIAGRAMS

## 1. User Account State Transition Diagram
![User Account State Transition Diagram](Object-State-Modeling%20Screenshots/user-account.png)

**Detailed Explanation**  
* **Key States**: Unregistered, PendingVerification, Active, Suspended, Deactivated.  
* **Key Transitions & Events**: Registration with guard (email unique), email verification, admin suspension/reactivation, user deactivation.  
* **How it maps to requirements**: Directly models the full lifecycle in **[FR-001 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[UC: Create User Account in USE-CASE-SPECIFICATIONS.md](../../USE-CASE-SPECIFICATIONS.md)**. Supports **[US-001 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)** by ensuring secure onboarding for students in underserved communities. The PendingVerification state prevents fake accounts.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/user-account.draw.io)**

## 2. Course State Transition Diagram
![Course State Transition Diagram](Object-State-Modeling%20Screenshots/course.png)

**Detailed Explanation**  
* **Key States**: Draft, Published, Archived.  
* **Key Transitions & Events**: Publish only when content is complete (guard condition), archive, republish, or delete.  
* **How it maps to requirements**: Matches **[FR-002 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[UC: Create Course in USE-CASE-SPECIFICATIONS.md](../../USE-CASE-SPECIFICATIONS.md)**. Supports **[US-006 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)** so instructors can control when courses go live, giving students reliable, high-quality content.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/course.draw.io)**

## 3. Enrollment State Transition Diagram
![Enrollment State Transition Diagram](Object-State-Modeling%20Screenshots/enrollment.png)

**Detailed Explanation**  
* **Key States**: Pending, Active, Completed, Dropped.  
* **Key Transitions & Events**: Confirmation after authentication, course completion, or drop.  
* **How it maps to requirements**: Tracks the Enrollment object per **[FR-002 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[UC: Enrol Course in USE-CASE-SPECIFICATIONS.md](../../USE-CASE-SPECIFICATIONS.md)**. Links directly to **[US-004 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)** and enables progress tracking for certifications.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/enrollment.draw.io)**

## 4. Quiz State Transition Diagram
![Quiz State Transition Diagram](Object-State-Modeling%20Screenshots/quiz.png)

**Detailed Explanation**  
* **Key States**: Draft, Published, Archived.  
* **Key Transitions & Events**: Publish after review (guard condition), archive.  
* **How it maps to requirements**: Supports instructor-side quiz management in **[FR-003 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[UC: Create Quiz in USE-CASE-SPECIFICATIONS.md](../../USE-CASE-SPECIFICATIONS.md)**. Aligns with **[US-007 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)**.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/quiz.draw.io)**

## 5. Quiz Attempt State Transition Diagram
![Quiz Attempt State Transition Diagram](Object-State-Modeling%20Screenshots/attempt-quiz.png)

**Detailed Explanation**  
* **Key States**: NotStarted, InProgress, Submitted, Graded, Passed, Failed.  
* **Key Transitions & Events**: Start quiz, submit (with time guard), auto-grade, outcome based on pass mark.  
* **How it maps to requirements**: Student-facing assessment flow from **[FR-003 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[UC: Take Quiz in USE-CASE-SPECIFICATIONS.md](../../USE-CASE-SPECIFICATIONS.md)**. Perfectly matches **[US-008 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)**.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/attempt-quiz.draw.io)**

## 6. Payment State Transition Diagram
![Payment State Transition Diagram](Object-State-Modeling%20Screenshots/payment.png)

**Detailed Explanation**  
* **Key States**: Initiated, Pending, Successful, Failed, Refunded.  
* **Key Transitions & Events**: Gateway calls, success/fail, retry, and refund.  
* **How it maps to requirements**: Full payment lifecycle in **[FR-005 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[UC: Process Payment in USE-CASE-SPECIFICATIONS.md](../../USE-CASE-SPECIFICATIONS.md)**. Supports **[US-010 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)** with secure third-party integration.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/payment.draw.io)**

## 7. Certification State Transition Diagram
![Certification State Transition Diagram](Object-State-Modeling%20Screenshots/certification.png)

**Detailed Explanation**  
* **Key States**: Requested, Awarded, Expired.  
* **Key Transitions & Events**: Awarded only when both payment and course are complete (guard condition).  
* **How it maps to requirements**: Ties directly to **[FR-005 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[US-010 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)**. Prevents invalid certifications.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/certification.draw.io)**

## 8. Notification State Transition Diagram
![Notification State Transition Diagram](Object-State-Modeling%20Screenshots/notification.png)

**Detailed Explanation**  
* **Key States**: Queued, Sent, Failed.  
* **Key Transitions & Events**: Send attempt with retry logic (max 3 attempts).  
* **How it maps to requirements**: Supports **[FR-006 in SYSTEM-REQUIREMENTS.md](../../SYSTEM-REQUIREMENTS.md)** and **[US-011 in AGILE-PLANNING.md](../../AGILE-PLANNING.md)** for reliable student/instructor updates.

**[Open Editable draw.io File in Browser](https://app.diagrams.net/#Hkeo-codes/the-it-code-academy/main/Assignment%208/Object-State-Modeling%20Drawio%20Files/notification.draw.io)**
