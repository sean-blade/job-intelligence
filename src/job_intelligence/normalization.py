import json
import re
from pathlib import Path
from urllib.parse import urlparse, urlunparse

DEFAULT_ALIASES_FILE = Path("config/aliases.json")
DEFAULT_EDUCATION_FILE = Path("config/education.json")


def load_aliases(aliases_file: Path = DEFAULT_ALIASES_FILE) -> dict[str, list[str]]:
    with open(aliases_file, "r", encoding="utf-8") as file:
        return json.load(file)


def normalize_skill(skill: str, aliases_file: Path = DEFAULT_ALIASES_FILE) -> str:

    skill = skill.lower().strip()

    aliases = load_aliases(aliases_file)

    for canonical, variations in aliases.items():
        if skill == canonical:
            return canonical

        if skill in variations:
            return canonical

    return skill


def skill_in_text(
    skill: str, text: str, aliases_file: Path = DEFAULT_ALIASES_FILE
) -> bool:
    aliases = load_aliases(aliases_file=aliases_file)
    skill = skill.lower().strip()
    text = text.lower()
    terms = [skill]
    if skill in aliases:
        terms.extend(aliases[skill])

    for term in terms:
        term_text = term.lower().strip()
        if not term_text:
            continue
        pattern = re.compile(rf"(?<!\w){re.escape(term_text)}(?!\w)")
        if pattern.search(text):
            return True

    return False


def edu_in_text(edu: str, text: str, edu_config: Path = DEFAULT_EDUCATION_FILE) -> bool:
    aliases = load_aliases(aliases_file=edu_config)
    edu = edu.lower()
    text = text.lower()
    terms = [edu]
    if edu in aliases:
        terms.extend(aliases[edu])

    return any(term.lower() in text for term in terms)


def hourly_to_annual(hourly_wage: float) -> int:
    """Convert an hourly wage to its full-time annual equivalent."""
    return round(hourly_wage * 2_080)


def normalize_url(url: str) -> str:
    parsed = urlparse(url)

    return urlunparse(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            parsed.path.rstrip("/"),
            "",
            "",
            "",
        )
    )
