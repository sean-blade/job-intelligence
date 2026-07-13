import json
from .models import JobPosting
from pathlib import Path


DEFAULT_SKILLS_FILE = Path("config/skills.json")

def load_skills(filepath: Path = DEFAULT_SKILLS_FILE) -> list[str]:
    """
    Load known skills from a JSON file.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_skills(description: str) -> list[str]:
    """
    Extract known skills from a job description.
    """
    skills = load_skills()

    description_lower = description.lower()

    found_skills = []

    for skill in skills:
        if skill in description_lower:
            found_skills.append(skill)

    return found_skills


def parse_job_description(
    title: str,
    company: str,
    location: str,
    description: str,
) -> JobPosting:
    """
    Convert raw job information into a JobPosting object.
    """

    skills = extract_skills(description)

    return JobPosting(
        title=title,
        company=company,
        location=location,
        description=description,
        skills=skills,
    )