import html
import re

import requests

from job_intelligence.ingestion.base import JobConnector
from job_intelligence.models import JobPosting


class GreenhouseConnector(JobConnector):
    def __init__(self, board: str):
        super().__init__(board=board)
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
                    company=self._extract_company(item),
                    location=item.get("location", {}).get("name"),
                    description=self._clean_description(item.get("content", "")),
                )
            )

        return jobs

    def _extract_company(self, item: dict) -> str | None:
        return (
            item.get("company", {}).get("name")
            or item.get("company_name")
            or self.board
        )

    def _clean_description(self, description: str | None) -> str | None:
        if description is None:
            return None

        decoded = html.unescape(description)
        stripped = re.sub(r"<[^>]+>", "", decoded)
        return " ".join(stripped.split())
