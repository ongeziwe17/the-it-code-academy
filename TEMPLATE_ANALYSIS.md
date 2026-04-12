# TEMPLATE ANALYSIS AND SELECTION

I spent time exploring GitHub’s project templates to find the best fit for THE IT CODE ACADEMY platform. I compared four templates that seemed most relevant to our Agile development process.

### Comparison Table

| Template              | Columns / Workflow                          | Automation Features                          | Suitability for THE IT CODE ACADEMY                          | Score (out of 10) |
|-----------------------|---------------------------------------------|----------------------------------------------|----------------------------------------------------------|-------------------|
| Basic Kanban          | To Do, In Progress, Done                    | None (manual only)                           | Too basic – I would waste time moving cards manually     | 6/10 |
| Automated Kanban      | To Do, In Progress, Review, Done            | Auto-moves issues when opened/closed/merged  | Perfect match for our sprint workflow                    | **9.5/10** |
| Bug Triage            | New, Needs Info, Triaged, In Progress, Done | Auto-labelling and assignment rules          | Too bug-focused, not ideal for feature development       | 4/10 |
| Team Planning         | Backlog, Planning, In Progress, Review, Done| Custom fields + priority sorting             | Good for planning but lacks automation during sprints    | 8/10 |

**Justification**  
I chose the **Automated Kanban** template because it already existed in our repository from Assignment 6. Its built-in automation (automatically moving cards when issues or pull requests change status) saves a lot of manual work and aligns perfectly with our sprint-based development. I then customised it by adding three new columns (Code Review, Testing, Blocked) to better support the quality needs of an educational platform. This choice gives us both automation and the flexibility we need for real Agile delivery.
