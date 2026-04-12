# PROJECT TEMPLATES & KANBAN BOARD IMPLEMENTATION
   
**GitHub Project Board:** [THE IT CODE ACADEMY BACKLOG → Sprint 1 View](https://github.com/keo-codes/the-it-code-academy/projects)  

---

## TEMPLATE ANALYSIS AND SELECTION

When I started this assignment I took time to properly explore GitHub’s built-in project templates. I wanted to choose one that would actually help me manage THE IT CODE ACADEMY development rather than just look good for the assignment.

### Comparison of GitHub Project Templates

| Template              | Columns / Workflow                          | Automation Features                          | Suitability for Agile (IT Code Academy)                  | Score (out of 10) |
|-----------------------|---------------------------------------------|----------------------------------------------|----------------------------------------------------------|-------------------|
| **Basic Kanban**      | To Do, In Progress, Done                    | None – fully manual                          | Simple but I would spend too much time moving cards manually | 6/10 |
| **Automated Kanban**  | To Do, In Progress, Review, Done            | Auto-moves issues when opened/closed/merged; status sync with PRs | Excellent – matches our sprint workflow and saves time | **9.5/10** |
| **Bug Triage**        | New, Needs Info, Triaged, In Progress, Done | Auto-labelling and assignment rules          | Too focused on bugs; not ideal for building learning features | 4/10 |
| **Team Planning**     | Backlog, Planning, In Progress, Review, Done| Custom fields + priority sorting             | Good for planning but lacks the automation I need during sprints | 8/10 |

**Justification for my choice**  
I selected the **Automated Kanban** template (which our existing “THE IT CODE ACADEMY BACKLOG” project was already based on). It feels like the perfect fit for our project because development is sprint-based and issue-heavy. The built-in automation means cards move automatically when I merge a pull request or close an issue — this reduces busywork and keeps the focus on delivering value to students.  

I then customized it further (see Section 2) to make it even more relevant to an online learning platform.

---

## CUSTOM KANBAN BOARD CREATION 

**Project Used:**  
[THE IT CODE ACADEMY BACKLOG – Sprint 1 View](https://github.com/keo-codes/the-it-code-academy/projects) (Automated Kanban template)

**Customizations I made**  
I added **three new columns** to better reflect real development stages for THE IT CODE ACADEMY:

- **Code Review** – to catch quality issues before features reach students  
- **Testing** – to ensure everything works smoothly for end users  
- **Blocked** – to make visible any tasks waiting on external input (e.g. content approval or API issues)

These columns go beyond the default template and directly address the quality needs of an educational platform.

**Screenshot of the customized Kanban board**  
*Screenshort*

**README Section – Why I customized the board this way**  
I started from the Automated Kanban template because its automation aligns perfectly with our Agile process from Assignment 6. However, the default columns didn’t fully capture the quality-focused workflow we need when building learning content.  

Adding **Code Review**, **Testing**, and **Blocked** made the board practical and meaningful:
- Code Review ensures educational accuracy (critical when instructors upload lessons and quizzes).
- Testing prevents bugs from reaching real students.
- Blocked gives immediate visibility when something is stuck.

I populated the board with the exact 6 user stories from my Assignment 6 Sprint 1 plan, linked each GitHub Issue, assigned tasks using `@keo-codes`, and applied consistent labels (`user-story`, `enhancement`, `must-have`).  

The result is a living, visual workflow that turns our static sprint plan into something I can actually use every day.

---

## KANBAN BOARD EXPLANATION 

**What is a Kanban board?**  
To me, a Kanban board is a visual map that shows exactly where every piece of work is in its journey — from idea to done.

**How our board works**  
- **Visualizes workflow**: The columns (Backlog → Ready → In Progress → Code Review → Testing → Blocked → Done) clearly show the stage of every task.
- **Limits Work-in-Progress (WIP)**: I keep a soft limit of 3 tasks in “In Progress” and “Code Review” so I don’t get overwhelmed and can finish things faster.
- **Supports Agile principles**: It encourages continuous flow, makes problems visible immediately, and lets me adapt priorities easily — exactly what Agile is about.

This board has already helped me stay focused while building THE IT CODE ACADEMY MVP.

---

## REFLECTION

Customizing this template was more challenging than I expected. At first I was tempted to just use Basic Kanban because it looked clean, but I realised it would create extra manual work every sprint. Choosing Automated Kanban and then adding my own columns felt like the right balance between automation and flexibility.

The hardest part was deciding what the new columns should be. I wanted them to feel natural to our education platform, not just random additions. Adding “Code Review”, “Testing”, and “Blocked” made the board genuinely useful instead of just an assignment requirement.

Compared to other tools:
- **Trello** is more visual and fun for quick brainstorming, but it doesn’t connect directly to GitHub Issues and PRs.
- **Jira** is extremely powerful with reports and epics, but it feels too heavy and corporate for a student project like ours.

GitHub Projects strikes the sweet spot — it’s free, lives inside our repo, and feels professional enough for real-world use.

This assignment helped me move from “just using GitHub” to thinking like a real project manager. I’m excited to keep improving this board as the IT Code Academy grows.

---
