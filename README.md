# Job Intelligence

A project for exploring automated job analysis and intelligence tools.

## Goals

- Analyze job postings against candidate profiles
- Identify relevant job opportunities
- Provide useful information for job search decisions

## Current Status

**Project Status:** Phase 2 Development
**Current Release:** v0.2.0

### Completed
- CSV job ingestion
- Candidate profile loading
- Skill extraction
- Skill normalization and aliases
- Candidate/job matching
- Job ranking
- Command-line interface
- Automated testing
- Automated project structure documentation
- Required vs preferred skill detection
- Skill category matching
- Match score explanations

### Planned

- Improved job description parsing
- Experience matching
- Education matching
- Candidate preferences
- Improved match explanations

### Requirements
Python version: 3.13

## Development Setup

```bash
git clone https://github.com/sean-blade/job-intelligence.git
cd job-intelligence
uv sync --all-extras
```

### 1. Create virtual environment:

```bash
python -m venv .venv
```

### 2. Activate virtual environment:

Windows (Git Bash)
```bash
source .venv/Scripts/activate
```
Linux
```bash
source .venv/bin/activate
```
### 3. Install dependencies:

```bash
pip install -e ".[dev]"
```

### 4. Install Pre-commit hooks
```bash
pre-commit install
```
 
## Running

Analyze jobs:

```bash
python -m job_intelligence analyze data/sample_jobs.csv
```
Match jobs against specific candidate profile:
```bash
python -m job_intelligence match data/sample_jobs.csv
```
## Testing
Functional verification
```bash
pytest
```
Linting and Formatting
```bash
pre-commit run --all-files
```
## Project Structure
<!-- PROJECT_STRUCTURE_START -->

```text
job-intelligence/
├── .github/
│   └── workflows/
│       ├── quality.yml
│       └── tests.yml
├── config/
│   ├── aliases.json
│   ├── candidate.json
│   ├── categories.json
│   ├── education.json
│   └── skills.json
├── data/
│   ├── sample_candidate.json
│   └── sample_jobs.csv
├── src/
│   └── job_intelligence/
│       ├── ingestion/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── csv_connector.py
│       │   ├── greenhouse_connector.py
│       │   └── registry.py
│       ├── processing/
│       │   ├── __init__.py
│       │   ├── filters.py
│       │   └── pipeline.py
│       ├── __init__.py
│       ├── __main__.py
│       ├── analysis.py
│       ├── candidate_loader.py
│       ├── category.py
│       ├── cli.py
│       ├── education.py
│       ├── loader.py
│       ├── main.py
│       ├── matcher.py
│       ├── models.py
│       ├── normalization.py
│       ├── parser.py
│       ├── rank_jobs.py
│       ├── report.py
│       ├── salary.py
│       └── scoring.py
├── tests/ (...)
├── tools/ (...)
├── .gitignore
├── .pre-commit-config.yaml
├── AGENTS.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── README.md
├── ROADMAP.md
├── TODO.md
├── uv.lock
└── VISION.md
```

<!-- PROJECT_STRUCTURE_END -->
## Features

- [x] Collect job posting data from files
- [x] Extract skills from job descriptions
- [x] Match candidate profiles to job postings
- [x] Rank jobs by compatibility
- [x] Generate match reports

Future:
- [ ] Automated job collection
- [ ] Job market trend analysis
- [ ] Web dashboard
- [ ] Application tracking

## License

This project is licensed under the MIT License. See LICENSE for details.