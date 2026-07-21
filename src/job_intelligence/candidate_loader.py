import json
from pathlib import Path
from job_intelligence.models import CandidateProfile

DEFAULT_CANDIDATE_FILE = Path("config/candidate.json")


def load_candidate(filepath: Path | None = None) -> CandidateProfile:
    """
    Load a candidate profile from a JSON file.
    """
    if filepath is None:
        filepath = DEFAULT_CANDIDATE_FILE

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    skills = [skill.lower() for skill in data["skills"]]
    return CandidateProfile(
        name=data["name"], skills=skills, education=data.get("education", [])
    )
