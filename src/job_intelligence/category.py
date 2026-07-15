import json
from pathlib import Path

DEFAULT_CATEGORY_FILE = Path("config/categories.json")

def load_categories(file_path: Path = DEFAULT_CATEGORY_FILE) -> dict[str, list[str]]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
def categorize_skill(skill: str, categories_file: Path =DEFAULT_CATEGORY_FILE) -> str | None:
    categories = load_categories(categories_file)
    skill = skill.lower()
    for category, skills in categories.items():
        if skill in skills:
            return category
    return None