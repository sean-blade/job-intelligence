from collections import Counter

from .models import JobPosting
from .category import categorize_skill

def skill_frequency(jobs: list[JobPosting]) -> dict[str, int]:
    """
    Count how often each skill appears across job postings.
    """
    skills = []

    for job in jobs:
        skills.extend(job.extracted_skills.required)

    return dict(Counter(skills))

def skill_prevalence(jobs: list[JobPosting]) -> dict[str, float]:
    """
    Calculate the prevalence of each skill across job postings.
    """
    if not jobs:
        return {}
    for job in jobs:
        for skill in job.extracted_skills.required:
            if not isinstance(skill, str):
                raise ValueError(f"Skill must be a string, got {type(skill)}: {skill}")
    
    frequencies = skill_frequency(jobs)
    total_jobs = len(jobs)
    
    return {skill: count / total_jobs for skill, count in frequencies.items()}

def categorize_prevalance(jobs) -> dict[str, float]:
    """
    Categorize skills and calculate their prevalence across job postings.
    """
    category_count = {}
    total_jobs = len(jobs)

    for job in jobs:
        categories = set()
        for skill in job.extracted_skills.required:
            category = categorize_skill(skill)
            if category:
                categories.add(category)
        for category in categories:
            category_count[category] = category_count.get(category, 0) + 1

    return {category: count / total_jobs for category, count in category_count.items()}