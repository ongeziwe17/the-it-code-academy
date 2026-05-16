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
- Triggers on push/PR
- Python setup, linting (flake8), tests (pytest)
- Workflow: `.github/workflows/ci-cd.yml`

### 3. CD Pipeline 
- Builds Python release artifacts (`python -m build`)
- Uploads artifacts on merge to `main`

### 4. Documentation 
- README
- All work done via Pull Requests

## Pipeline Status
CI/CD workflow successfully running on GitHub Actions.

## CI/CD Pipeline with GitHub Actions

### How to Run Tests Locally
```bash
cd Assignment\ 12
pip install -r requirements.txt
python -m pytest tests/ -v
