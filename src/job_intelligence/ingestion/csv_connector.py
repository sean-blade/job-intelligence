# csv_connector.py

from job_intelligence.ingestion.base import JobConnector
from job_intelligence.loader import load_jobs_from_csv
from job_intelligence.models import JobPosting


class CSVConnector(JobConnector):

    def __init__(self, path: str):
        super().__init__(path=path)
        self.path = path

    @property
    def source_name(self) -> str:
        return "csv"

    def fetch_jobs(self) -> list[JobPosting]:
        return load_jobs_from_csv(self.path)
