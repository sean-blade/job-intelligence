## Todos
- [ ] reorganize files in job_intelligence and refactor
- [ ] job filter for relevancy
- [ ] salary score penalty
- [ ] in greenhouse connector, clean up html entities
- [ ] check education extractor to see if it is supposed to output all levels
- [ ] extractor for skills needs to be checked to see why a few skills if any are pulled
- [ ] every connector should populate source, source_id, board (ex: greenhouse, stripe, stripe)
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