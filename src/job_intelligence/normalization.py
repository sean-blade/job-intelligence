import json
from pathlib import Path


DEFAULT_ALIASES_FILE = Path("config/aliases.json")


def normalize_skill(
    skill: str,
    aliases_file: Path = DEFAULT_ALIASES_FILE
) -> str:

    skill = skill.lower().strip()

    with open(aliases_file, "r", encoding="utf-8") as file:
        aliases = json.load(file)

    for canonical, variations in aliases.items():
        if skill == canonical:
            return canonical

        if skill in variations:
            return canonical

    return skill