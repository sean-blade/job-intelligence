from job_intelligence.models import JobPosting

ENGINEERING_TERMS = [
    "engineer",
    "engineering",
    "developer",
    "software",
    "mechanical",
    "biomedical",
    "hardware",
]


def is_relevant_job(job: JobPosting) -> bool:
    text = f"{job.title} {job.description}".lower()

    return any(term in text for term in ENGINEERING_TERMS)


def filter_jobs(jobs: list[JobPosting]) -> list[JobPosting]:
    for job in jobs:
        job.relevant = is_relevant_job(job)
    return jobs
