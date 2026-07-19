import json
from pathlib import Path
from job_intelligence.models import CandidateProfile


def load_candidate(filepath: Path) -> CandidateProfile:
    """
    Load a candidate profile from a JSON file.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    skills = [skill.lower() for skill in data["skills"]]
    return CandidateProfile(
        name=data["name"], skills=skills, education=data["education"]
    )
