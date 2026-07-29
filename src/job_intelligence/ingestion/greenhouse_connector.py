import html
import re
from pathlib import Path

import requests

from job_intelligence.ingestion.base import JobConnector
from job_intelligence.models import JobPosting
from job_intelligence.parser import parse_job_description


class GreenhouseConnector(JobConnector):
    def __init__(self, board: str, skills_file: str | Path | None = None):
        super().__init__(board=board)
        self.board = board
        self.skills_file = Path(skills_file) if skills_file is not None else None

    @property
    def source_name(self) -> str:
        return "greenhouse"

    def fetch_jobs(self) -> list[JobPosting]:
        url = (
            f"https://boards-api.greenhouse.io/v1/boards/"
            f"{self.board}/jobs?content=true"
            # https://boards-api.greenhouse.io/v1/boards/stripe/jobs?content=true example job board
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        jobs: list[JobPosting] = []

        for item in data["jobs"]:
            cleaned_description = self._clean_description(item.get("content", "")) or ""
            parse_kwargs = {
                "title": item.get("title"),
                "company": self._extract_company(item),
                "location": item.get("location", {}).get("name"),
                "description": cleaned_description,
            }
            if self.skills_file is not None:
                parse_kwargs["skills_file"] = self.skills_file

            jobs.append(parse_job_description(**parse_kwargs))

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
