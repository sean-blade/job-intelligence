from .models import JobPosting


COMMON_SKILLS = [
    "python",
    "matlab",
    "sql",
    "machine learning",
    "finite element analysis",
    "fea",
    "cad",
]


def extract_skills(description: str) -> list[str]:
    """
    Extract known skills from a job description.
    """

    description_lower = description.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
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