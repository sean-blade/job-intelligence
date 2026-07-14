# Job Intelligence

A project for exploring automated job analysis and intelligence tools.

## Goals

- Collect and process job information
- Analyze job descriptions
- Extract useful trends and insights

## Development Setup

Python version: 3.13

### Create virtual environment:

```bash
python -m venv .venv
```

### Activate:

Windows
```bash
source .venv/Scripts/activate
```
Linux
```bash
source .venv/bin/activate
```
### Install dependencies:

```bash
pip install -r requirements.txt
```
### Running

```bash
python -m job_intelligence
```
### Testing

```bash
pytest
```
## Project Structure
<!-- PROJECT_STRUCTURE_START -->

```text
job-intelligence/
├── .pytest_cache/
│   ├── v/
│   │   └── cache/
│   │       ├── lastfailed
│   │       └── nodeids
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   └── README.md
├── config/
│   ├── aliases.json
│   └── skills.json
├── data/
│   ├── sample_candidate.json
│   └── sample_jobs.csv
├── src/
│   ├── job_intelligence/
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── analysis.py
│   │   ├── candidate.py
│   │   ├── candidate_loader.py
│   │   ├── cli.py
│   │   ├── loader.py
│   │   ├── main.py
│   │   ├── matcher.py
│   │   ├── models.py
│   │   ├── normalization.py
│   │   ├── parser.py
│   │   ├── rank_jobs.py
│   │   └── report.py
│   └── job_intelligence.egg-info/
│       ├── dependency_links.txt
│       ├── PKG-INFO
│       ├── requires.txt
│       ├── SOURCES.txt
│       └── top_level.txt
├── tests/
│   ├── test_analysis.py
│   ├── test_candidate_loader.py
│   ├── test_cli.py
│   ├── test_loader.py
│   ├── test_main.py
│   ├── test_matcher.py
│   ├── test_models.py
│   ├── test_normalize.py
│   ├── test_parser.py
│   ├── test_rank_jobs.py
│   └── test_report.py
├── tools/
│   └── update_structure_readme.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

<!-- PROJECT_STRUCTURE_END -->
## Features

- [ ] Collect job posting data
- [ ] Extract skills and requirements
- [ ] Analyze job trends
- [ ] Match candidate profiles to job postings
- [ ] Generate job market insights