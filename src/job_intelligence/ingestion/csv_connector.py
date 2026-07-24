# csv_connector.py

from job_intelligence.ingestion.base import JobConnector
from job_intelligence.loader import load_jobs_from_csv
from job_intelligence.models import JobPosting


class CSVConnector(JobConnector):
    @property
    def source_name(self) -> str:
        return "csv"

    def __init__(self, path: str):
        self.path = path

    def fetch_jobs(self) -> list[JobPosting]:
        return load_jobs_from_csv(self.path)
