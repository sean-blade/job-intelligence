## Todos

- [ ] check education extractor to see if it is supposed to output all levels
- [ ] every connector should populate source, source_id, board (ex: greenhouse, stripe, stripe)
- [ ] relevance of job filtering
- [ ] rank stored jobs
- [ ] display results

## Deferred tasks
- [ ] reorganize files in job_intelligence and refactor

## Pipeline Status

Greenhouse fetch                WORKING
CSV fetch                       WORKING
JobPosting conversion           WORKING
Requirement extraction          WORKING, with accuracy limitations
Relevance filtering             PARTIAL
SQLite save/load                WORKING
CLI database integration        WORKING
Duplicate handling              DEFERRED
Load SQLite into matcher        NOT STARTED
Rank real stored jobs           NOT STARTED
Generate final real-data report PARTIAL
Salary scoring penalty          DEFERRED

<!--
src/job_intelligence/

├── models.py

├── ingestion/
│   ├── base.py
│   ├── csv_connector.py
│   ├── greenhouse_connector.py
│   └── registry.py

├── analysis/
│   ├── __init__.py
│   ├── skills.py
│   └── categories.py

├── matching/
│   ├── __init__.py
│   ├── matcher.py
│   ├── scoring.py
│   └── ranking.py

├── extraction/
│   ├── __init__.py
│   ├── education.py
│   ├── salary.py
│   └── parser.py

├── processing/
│   ├── __init__.py
│   └── filters.py

├── io/
│   ├── candidate_loader.py
│   └── report.py
-->