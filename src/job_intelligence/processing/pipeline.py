from job_intelligence.models import JobPosting
from job_intelligence.processing.filters import is_relevant_job


def process_jobs(jobs: list[JobPosting]) -> list[JobPosting]:
    for job in jobs:
        job.relevant = is_relevant_job(job)

    return jobs
