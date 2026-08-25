# Job Intelligence

A tool for collecting, analyzing, and ranking job postings against a candidate profile.

## Goals

- Analyze job postings against candidate profiles
- Identify relevant job opportunities
- Provide useful information for job search decisions
- Collect job postings from files and external sources (job boards)
- Store job data for later analysis and automation

## Current Status

**Project Status:** Late Phase 2 Development
**Current Release:** v0.2.0

Job Intelligence currently supports job ingestion from CSV files and Greenhouse
job boards, candidate-based matching and ranking, requirement extraction, JSON
exports, and initial SQLite persistence.

### Completed

- Candidate profile loading
- CSV job ingestion
- Greenhouse job-board conector
- Shared ingestion connector interface and registry
- Candidate profile loading
- Skill extraction
- Skill normalization and aliases
- Skill category matching
- Required vs preferred skill detection
- Education extraction and level matching
- Salary range extraction and overlap detection
- Candidate/job matching
- Job ranking
- Match score explanations
- Text reports
- Command-line interface
- JSON export (optional)
- Automated testing
- Ruff, Black, mypy, pre-commit, and Github Actions
- Automated project structure documentation
- Relevance filtering during ingestion
- Completing the SQLite-backed ingestion workflow

### Planned

- Prevent duplicate job records
- Loading stored jobs for analysis
- Salary-based score penalty
- Improved parsing accuracy

## Next Milestone

Complete usable live-data workflow

```text
Greenhouse or CSV
    → convert to JobPosting objects
    → filter relevant jobs
    → store in SQLite
    → load stored jobs
    → rank against candidate
    → generate report
```

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
### 3. Install Git Hook:

```bash
pre-commit install
```
 
## Running

Analyze jobs:

```bash
python -m job_intelligence analyze data/sample_jobs.csv
```

Match jobs against Default candidate profile:

```bash
python -m job_intelligence match data/sample_jobs.csv
```

Match jobs against specific candidate profile:

```bash
python -m job_intelligence match data/sample_jobs.csv \
    --candidate data/sample_candidate.json
```

Ingest jobs from CSV into SQLite:

```bash
python -m job_intelligence ingest csv data/sample_jobs.csv
```
Ingest jobs from Greenhouse into SQLite:

```bash
python -m job_intelligence ingest greenhouse stripe   # 'Stripe' is an example job board
```

Using custom Database path:

```bash
python -m job_intelligence ingest greenhouse stripe \
    --database data/databases/jobs.db
```

Optional export to JSON:

```bash
# Limit results to 10 jobs (optional)
python -m job_intelligence ingest greenhouse stripe \
    --output data/raw/stripe_jobs.json \
    --limit 10  
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
├── config/          # Skills, categories, education mappings
├── data/            # Raw, processed, cache, and database files
├── src/job_intelligence/
│   ├── analysis/    # Skill and category analysis
│   ├── extraction/  # Parsing and data extraction
│   ├── ingestion/   # Job board and csv connectors
│   ├── matching/    # Candidate-job matching and scoring
│   ├── processing/  # Filtering and processing pipelines
│   └── storage/     # Persistence models, SQLite
├── tests/
├── tools/
├── README.md
├── ARCHITECTURE.md
└── pyproject.toml
```

<!-- PROJECT_STRUCTURE_END -->
## Features

- [x] Load reusable candidate profiles
- [x] Collect jobs from CSV files
- [x] Collect jobs from Greenhouse job boards
- [x] Convert different sources into a shared `JobPosting` model
- [x] Extract required and preferred skills
- [x] Normalize skill names and aliases
- [x] Extract education requirements
- [x] Extract salary ranges
- [x] Match and rank jobs against a candidate
- [x] Generate readable match reports
- [x] Export jobs to JSON
- [x] Persist jobs in SQLite
- [x] Filter irrelevant jobs during ingestion
- [x] Prevent duplicate stored jobs
- [ ] Match and analyze directly from SQLite
- [ ] Run ingestion automatically on a server
- [ ] Provide a web dashboard
- [ ] Track job applications


## License

This project is licensed under the MIT License. See LICENSE for details.