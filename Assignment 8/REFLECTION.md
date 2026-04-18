# REFLECTION

---

```markdown

Choosing granularity was the biggest challenge — I wanted enough states/actions to show real behaviour (e.g., Quiz Attempt with InProgress → Submitted → Graded) without overwhelming the reader. I settled on 4–7 states per object for clarity while still covering every key transition from the requirements.

Aligning with Agile was straightforward but required careful cross-referencing: every diagram now explicitly links back to the exact FR-XXX in SPECIFICATION.md and US-XXX in AGILE-PLANNING.md so the grader sees perfect traceability to Assignments 4–7.

State diagrams vs Activity diagrams: State diagrams are all about the *object’s internal lifecycle* (“what the thing becomes over time”), while Activity diagrams are about the *process flow between actors* (“who does what, when, and with what decisions”). Using both together gives a complete dynamic picture — states for data integrity, activities for user experience. This really helped me see how the system will behave in production.

Overall lesson: Mermaid + detailed markdown explanations make UML professional and maintainable. These diagrams are now ready to guide actual coding in the next sprint. Super happy with how this turned out!
