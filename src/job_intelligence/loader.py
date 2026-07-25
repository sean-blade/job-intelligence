import csv
import json
from dataclasses import asdict
from pathlib import Path
from .parser import parse_job_description
from .models import JobPosting


def load_jobs_from_csv(filepath: str | Path) -> list[JobPosting]:
    """
    Load job postings from a CSV file.
    """

    jobs = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            job = parse_job_description(
                title=row["title"],
                company=row["company"],
                location=row["location"],
                description=row["description"],
                skills_file=Path("config/skills.json"),
            )

            jobs.append(job)

    return jobs


def save_jobs_to_json(jobs: list[JobPosting], filepath: str | Path) -> None:
    """Save a list of job postings to a JSON file."""

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump([asdict(job) for job in jobs], file, indent=2)
