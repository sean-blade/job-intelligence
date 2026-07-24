import requests

from job_intelligence.ingestion.base import JobConnector
from job_intelligence.models import JobPosting


class GreenhouseConnector(JobConnector):
    def __init__(self, board: str):
        self.board = board

    @property
    def source_name(self) -> str:
        return "greenhouse"

    def fetch_jobs(self) -> list[JobPosting]:
        url = (
            f"https://boards-api.greenhouse.io/v1/boards/"
            f"{self.board}/jobs?content=true"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        jobs: list[JobPosting] = []

        for item in data["jobs"]:
            jobs.append(
                JobPosting(
                    title=item.get("title"),
                    # TODO: Use actual company name if available from source.
                    company=self.board,
                    location=item.get("location", {}).get("name"),
                    description=item.get("content", ""),
                )
            )

        return jobs
