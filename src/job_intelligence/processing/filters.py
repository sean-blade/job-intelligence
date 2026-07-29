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
    return [job for job in jobs if is_relevant_job(job)]


# TODO: add relevant as param to jobposting class to filter view, prevent destruction of information.
