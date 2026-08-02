from pathlib import Path

from job_intelligence.ingestion.greenhouse_connector import GreenhouseConnector
from job_intelligence.storage.sqlite_store import SQLiteStore

connector = GreenhouseConnector("stripe")
jobs = connector.fetch_jobs()

store = SQLiteStore(Path("jobs.db"))
store.save_jobs(jobs)

loaded_jobs = store.load_jobs()

print(f"Saved {len(jobs)} jobs")
print(f"Loaded {len(loaded_jobs)} jobs")
print(loaded_jobs[0])

store.close()
