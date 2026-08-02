from pathlib import Path
import sqlite3
from job_intelligence.models import JobPosting


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
                description TEXT
            )
        """)

        self.connection.commit()

    def save_jobs(self, jobs: list[JobPosting]):
        for job in jobs:
            self.cursor.execute(
                """
                INSERT INTO jobs (title, company, location, description) VALUES (?, ?, ?, ?)
                """,
                (job.title, job.company, job.location, job.description),
            )

        self.connection.commit()

    def load_jobs(self) -> list[JobPosting]:
        self.cursor.execute("SELECT title, company, location, description FROM jobs")
        rows = self.cursor.fetchall()
        jobs = []
        for row in rows:
            job = JobPosting(
                title=row[0], company=row[1], location=row[2], description=row[3]
            )
            jobs.append(job)
        return jobs

    def close(self):
        self.connection.close()
