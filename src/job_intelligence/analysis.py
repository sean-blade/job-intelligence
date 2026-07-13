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

def skill_prevalence(jobs: list[JobPosting]) -> dict[str, float]:
    """
    Calculate the prevalence of each skill across job postings.
    """
    if not jobs:
        return {}
    
    frequencies = skill_frequency(jobs)
    
    total_jobs = len(jobs)
    
    return {
        skill: count / total_jobs 
        for skill, count in frequencies.items()
    }