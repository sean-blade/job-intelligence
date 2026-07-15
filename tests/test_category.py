from job_intelligence.category import load_categories, categorize_skill
from job_intelligence.normalization import normalize_skill

def test_load_categories():
    categories = load_categories()
    assert "programming" in categories
    assert "python" in categories["programming"]


def test_categorize_skill():
    assert categorize_skill("python") == "programming"
    assert categorize_skill("cad") == "engineering"


def test_unknown_skill_returns_none():
    assert categorize_skill("unicorn technology") is None


def test_aliases_work_with_categories():
    skill = normalize_skill("FEA")

    assert skill == "finite element analysis"
    assert categorize_skill(skill) == "engineering"