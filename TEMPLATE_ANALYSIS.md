# TEMPLATE ANALYSIS AND SELECTION

Before choosing a template, I took time to explore GitHub’s available project templates in detail. I wanted something that would genuinely support the ongoing development of THE IT CODE ACADEMY — an educational platform with sprints, user stories, and quality-focused features — rather than just ticking a box for the assignment.

I compared four templates that seemed most relevant:

### Comparison Table

| Template              | Columns / Workflow                                      | Automation Features                                      | Suitability for THE IT CODE ACADEMY (Agile Education Platform) | Score (out of 10) |
|-----------------------|---------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------|-------------------|
| Basic Kanban          | To Do, In Progress, Done                                | None – completely manual                                 | Too simple; I would spend too much time manually moving cards every day | 6/10 |
| Automated Kanban      | To Do, In Progress, Review, Done                        | Automatic card movement when issues are opened, closed, or PRs are merged | Excellent – matches our sprint workflow and reduces admin work | **9.5/10** |
| Bug Triage            | New, Needs Info, Triaged, In Progress, Done             | Auto-labelling, assignment rules, triage workflows       | Too narrowly focused on bugs; not suitable for feature development and lesson creation | 4/10 |
| Team Planning         | Backlog, Planning, In Progress, Review, Done            | Custom fields, priority sorting, planning views          | Strong for planning phases but weaker on automation during active sprints | 8/10 |

**Justification for my choice**  
I selected the **Automated Kanban** template because our “THE IT CODE ACADEMY BACKLOG” project was already based on it from Assignment 6. The built-in automation is a game-changer for me as a solo developer/student: when I close an issue or merge a pull request, the card moves automatically. This keeps the board accurate without extra effort and directly supports the Agile principle of continuous delivery.

The default template was good, but it didn’t fully reflect the quality steps needed for an educational platform (where accuracy in quizzes and lesson content is critical). That’s why I customised it by adding three new columns (see Custom Kanban Board section). This combination gives me the best of both worlds: automation from GitHub plus a workflow tailored to our specific needs. It feels professional and practical, not just an assignment requirement.

