import json
import sqlite3
from pathlib import Path

from job_intelligence.models import ExtractedSkills, JobPosting, SalaryRange


class SQLiteStore:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                relevant INTEGER NOT NULL DEFAULT 0,
                salary_min INTEGER,
                salary_max INTEGER,
                education TEXT NOT NULL DEFAULT '[]',
                required_skills TEXT NOT NULL DEFAULT '[]',
                preferred_skills TEXT NOT NULL DEFAULT '[]'
            )
            """)
        self.connection.commit()

    def save_jobs(self, jobs: list[JobPosting]):
        for job in jobs:
            salary_minimum = job.salary.minimum if job.salary else None
            salary_maximum = job.salary.maximum if job.salary else None

            self.cursor.execute(
                """
                INSERT INTO jobs (
                    title, 
                    company, 
                    location, 
                    description, 
                    relevant, 
                    salary_min, 
                    salary_max, 
                    education, 
                    required_skills, 
                    preferred_skills
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job.title,
                    job.company,
                    job.location,
                    job.description,
                    int(job.relevant),
                    salary_minimum,
                    salary_maximum,
                    json.dumps(job.education),
                    json.dumps(job.extracted_skills.required),
                    json.dumps(job.extracted_skills.preferred),
                ),
            )

        self.connection.commit()

    def load_jobs(self) -> list[JobPosting]:
        self.cursor.execute("""
            SELECT 
                title, 
                company, 
                location, 
                description, 
                relevant, 
                salary_min, 
                salary_max, 
                education, 
                required_skills, 
                preferred_skills 
            FROM jobs
            """)

        rows = self.cursor.fetchall()
        jobs: list[JobPosting] = []

        for row in rows:
            salary = (
                SalaryRange(minimum=row[5], maximum=row[6])
                if row[5] is not None or row[6] is not None
                else None
            )

            job = JobPosting(
                title=row[0],
                company=row[1],
                location=row[2],
                description=row[3],
                relevant=bool(row[4]),
                salary=salary,
                education=json.loads(row[7]) if row[7] else [],
                extracted_skills=ExtractedSkills(
                    required=json.loads(row[8]) if row[8] else [],
                    preferred=json.loads(row[9]) if row[9] else [],
                ),
            )

            jobs.append(job)

        return jobs

    def close(self) -> None:
        self.connection.close()
