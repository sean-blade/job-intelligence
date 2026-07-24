# Job Intelligence - Agent Context

## Goal
Build a Python tool that analyzes job postings and matches candidates to jobs.

## Current Status
MVP development. Prioritize working features over production complexity.

## Stack
- Python 3.13
- pytest
- ruff
- mypy
- GitHub Actions
- uv/pip environment management

## Architecture

src/job_intelligence/

models.py
- JobPosting
- CandidateProfile
- MatchResult

loader.py
- Load jobs from CSV
- Load candidate profiles

analysis.py
- Job market statistics
- Skill prevalence

matcher.py
- Candidate/job matching logic

cli.py
- Command line interface

## Design Philosophy
Avoid overengineering.
The goal is a working portfolio project quickly.

Prefer:
- simple functions
- readable code
- tests before large refactors

Avoid:
- unnecessary frameworks
- premature ML solutions
- complex abstractions

## Current Focus
Finish matching pipeline:
- skills extraction
- education extraction
- scoring
- CLI polish
- tests