# REFLECTION

Developing the domain model and class diagram for THE IT CODE ACADEMY was both challenging and deeply rewarding. As an Honors student who is passionate about using technology to create meaningful social impact, this assignment helped me connect abstract object-oriented concepts with the real needs of underserved young learners.

One of the main challenges I faced was striking the right balance between detail and clarity. Initially, I overloaded classes with too many attributes and methods, making the model feel cluttered. I also struggled with placing responsibilities correctly — for instance, deciding whether notifications should belong to the User class or be handled elsewhere. Through several iterations, I learned to focus on the core responsibilities of each entity and keep the domain model centered on business concepts rather than technical implementation.

Modelling the relationship between Students and Courses proved particularly tricky. A basic many-to-many link wasn’t sufficient because we needed to track individual progress, completion percentage, and certificate status. Introducing the Enrollment class as an association class was a key breakthrough that significantly improved the model’s expressiveness.

I was happy to see how well this design aligns with my previous assignments. The use cases from Assignment 5 (enrolling in courses, completing lessons, submitting assessments) map directly to the methods defined here. The state transitions from Assignment 8 are clearly supported by the status and completionPercentage fields in the Enrollment class. Even the practical constraints identified during Agile planning in Assignment 6, such as limiting students to five active courses, are enforced through multiplicity and business rules.

In terms of design trade-offs, I chose inheritance for Student and Instructor because they share substantial common behaviour. However, I kept the hierarchy shallow to preserve flexibility. I also favoured composition for the Course-Lesson relationship, which feels more natural and maintainable than deep inheritance.

This assignment reinforced several important lessons about object-oriented design. A strong domain model serves as the foundation for the entire system — it creates a shared language, reduces future refactoring effort, and makes the application much easier to extend. I now better understand the value of validating the domain model against use cases and behavioral diagrams early in the development process.

Most importantly, working on this model reminded me of the bigger purpose behind THE IT CODE ACADEMY. Every class and relationship exists to help young people in underserved communities gain valuable ICT and programming skills in a structured, supportive way. Seeing object-oriented principles directly support such a meaningful goal has been incredibly motivating.

