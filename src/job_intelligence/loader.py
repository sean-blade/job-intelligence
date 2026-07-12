import csv
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
            )

            jobs.append(job)

    return jobs