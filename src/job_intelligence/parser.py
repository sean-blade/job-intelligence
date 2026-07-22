import json
from .models import JobPosting, ExtractedSkills
from pathlib import Path
from .normalization import skill_in_text, edu_in_text

DEFAULT_SKILLS_FILE = Path("config/skills.json")
DEFAULT_EDUCATION_FILE = Path("config/education.json")


def load_skills(filepath: Path = DEFAULT_SKILLS_FILE) -> list[str]:
    """
    Load known skills from a JSON file.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def load_edu(filepath: Path = DEFAULT_EDUCATION_FILE) -> list[str]:
    """
    Load known education from a JSON file.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def split_description_sections(description: str) -> tuple[str, str]:
    """
    Split a job description into (required, preferred) sections.
    If no common heading is found, the entire description is treated as required
    and preferred is returned as an empty string.
    """
    PREFERRED_HEADING_TAGS = {
        "preferred qualifications",
        "preferred",
    }
    REQUIRED_HEADING_TAGS = {
        "required",
        "required qualifications",
        "minimum qualifications",
    }

    desc_lower = description.lower()

    # Find the earliest occurrence of any known heading
    required_idx = get_heading_idx(desc_lower, REQUIRED_HEADING_TAGS)
    preferred_idx = get_heading_idx(desc_lower, PREFERRED_HEADING_TAGS)

    if required_idx is None and preferred_idx is None:
        return (description, "")

    if required_idx is None:
        return (description, "")

    if preferred_idx is None:
        return (description, "")

    # Both indexes exist here
    if required_idx < preferred_idx:
        required = description[required_idx:preferred_idx]
        preferred = description[preferred_idx:]
    else:
        preferred = description[preferred_idx:required_idx]
        required = description[required_idx:]

    return (required, preferred)


def get_heading_idx(text, tags):
    text = text.lower()
    earliest_idx = None
    for tag in tags:
        tag = tag.lower()
        idx = text.find(tag)
        if idx != -1:
            if earliest_idx is None or idx < earliest_idx:
                earliest_idx = idx
    return earliest_idx


def extract_skills(
    description: str, skills_file: Path = DEFAULT_SKILLS_FILE
) -> ExtractedSkills:
    """
    Extract known skills from a job description.
    """
    skills = load_skills(skills_file)
    required, preferred = split_description_sections(description=description)
    required = required.lower()
    preferred = preferred.lower()

    required_skills = []
    preferred_skills = []

    for skill in skills:
        if skill_in_text(skill, required):
            required_skills.append(skill)

        if skill_in_text(skill, preferred):
            preferred_skills.append(skill)

    return ExtractedSkills(required=required_skills, preferred=preferred_skills)


def extract_education(
    description: str, edu_config: Path = DEFAULT_EDUCATION_FILE
) -> list[str]:
    education = load_edu(edu_config)
    description = description.lower()
    required_education = []
    for edu in education:
        if edu_in_text(edu, description):
            required_education.append(edu)
    return required_education


def parse_job_description(
    title: str,
    company: str,
    location: str,
    description: str,
    skills_file: Path = DEFAULT_SKILLS_FILE,
) -> JobPosting:
    """
    Convert raw job information into a JobPosting object.
    """

    extracted_skills = extract_skills(description, skills_file)
    # extracted_education = extract_education(description, edu_file)
    return JobPosting(
        title=title,
        company=company,
        location=location,
        description=description,
        extracted_skills=extracted_skills,
        # education=extracted_education
    )
