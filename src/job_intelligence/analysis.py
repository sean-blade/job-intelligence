from collections import Counter

from .models import JobPosting


def skill_frequency(jobs: list[JobPosting]) -> dict[str, int]:
    """
    Count how often each skill appears across job postings.
    """

    skills = []

    for job in jobs:
        skills.extend(job.skills)

    return dict(Counter(skills))