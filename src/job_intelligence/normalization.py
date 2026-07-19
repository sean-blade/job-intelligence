import json
from pathlib import Path

DEFAULT_ALIASES_FILE = Path("config/aliases.json")


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
    skill = skill.lower()
    text = text.lower()
    terms = [skill]
    if skill in aliases:
        terms.extend(aliases[skill])

    return any(term.lower() in text for term in terms)
