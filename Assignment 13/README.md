# IMPLEMENTING CI/CD WITH GITHUB ACTIONS

# IMPLEMENTING CI/CD WITH GITHUB ACTIONS

## Overview
Completed full CI/CD pipeline for **THE IT CODE ACADEMY** project using GitHub Actions.

## Deliverables

### 1. Branch Protection
- `main` branch protected
- Requires PR + 1 approval
- Requires status checks to pass
- See [PROTECTION.md](PROTECTION.md)

### 2. CI Pipeline
- Triggers on push and PR to `main`
- Sets up Python 3.11 + runs `pytest`
- Workflow: `.github/workflows/ci-cd.yml`

### 3. CD Pipeline
- On successful merge to `main`: creates release ZIP artifact
- Artifact uploaded via GitHub Actions

### 4. Documentation
- All changes made via Pull Requests
- Screenshots available in `Screenshots/` folder

## Pipeline Status
CI/CD workflow is active and successfully running.

## How to Run Tests Locally

```bash
cd "Assignment 12"
pip install -r requirements.txt
python -m pytest tests/ -v
```

## CI/CD Pipeline Overview

- **Branch Protection**: main branch protected (PR + approval + passing tests required).
- **CI Workflow**: Runs full test suite on every push and PR.
- **CD Workflow**: Automatically generates and uploads release artifact on merge to main.

**Pipeline Status**: Active and successfully running on GitHub Actions.

## Screenshots
All evidence available in the [Screenshots](Screenshots/) folder:

- Branch protection rules
- GitHub Actions workflow runs
- Release artifact generation
- PR workflow examples
