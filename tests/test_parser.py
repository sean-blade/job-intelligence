from job_intelligence.parser import (
    extract_skills,
    parse_job_description,
    split_description_sections,
    get_heading_idx,
    extract_education,
    extract_salary,
)
from job_intelligence.models import SalaryRange


def test_extract_skills(tmp_path):
    # Create a temporary skills file
    skills_file = tmp_path / "skills.json"
    skills_file.write_text(
        '["python", "matlab", "finite element analysis"]', encoding="utf-8"
    )

    description = """
    Looking for an engineer with Python,
    MATLAB, and finite element analysis experience.
    """

    skills = extract_skills(description, skills_file)

    assert "python" in skills.required
    assert "matlab" in skills.required
    assert "finite element analysis" in skills.required


def test_parse_job_description():
    job = parse_job_description(
        title="Biomedical Engineer",
        company="Example Corp",
        location="Remote",
        description="Experience with Python and CAD.",
    )

    assert job.title == "Biomedical Engineer"
    assert "python" in job.extracted_skills.required
    assert "cad" in job.extracted_skills.required


def test_custom_skill_file(tmp_path):
    # Create a temporary skills file
    skills_file = tmp_path / "skills.json"
    skills_file.write_text('["python", "docker"]', encoding="utf-8")

    description = "Looking for an engineer with Python and docker experience."
    result = extract_skills(description, skills_file=skills_file)

    assert result.required == ["python", "docker"]
    assert result.preferred == []


def test_required_before_preferred():
    description = """
        Required:
        Python
        Docker

        Preferred:
        CAD
        """
    required, preferred = split_description_sections(description)

    assert "Python" in required
    assert "Docker" in required
    assert "CAD" not in required
    assert "CAD" in preferred


def test_preferred_before_required():
    description = """
        Preferred:
        CAD

        Required:
        Python
        Docker
        """
    required, preferred = split_description_sections(description)

    assert "Python" in required
    assert "Docker" in required
    assert "CAD" not in required
    assert "CAD" in preferred


def test_only_preferred():
    description = """
        Preferred:
        CAD
        """
    required, preferred = split_description_sections(description)

    assert "CAD" in required
    assert preferred == ""


def test_no_headings():
    description = """
        CAD
        Python
        Docker
        """
    required, preferred = split_description_sections(description)

    assert "CAD" in required
    assert "Python" in required
    assert "Docker" in required
    assert preferred == ""


def test_empty_description():
    required, preferred = split_description_sections("")

    assert required == ""
    assert preferred == ""


def test_get_heading_idx_finds_heading():
    text = "hello required qualifications python"

    result = get_heading_idx(text, {"required", "required qualifications"})

    assert result == 6


def test_get_heading_idx_no_heading():
    text = "hello python"

    result = get_heading_idx(text, {"required", "preferred"})

    assert result is None


def test_extract_required_and_preferred_skills():

    description = """
    Required:
    Python
    MATLAB

    Preferred:
    CAD
    """

    result = extract_skills(description)

    assert result.required == ["python", "matlab"]

    assert result.preferred == ["cad"]


def test_extract_alias_skill():
    description = """Required:
     Experience with FEA and CAD
     """

    result = extract_skills(description=description)
    assert "finite element analysis" in result.required
    assert "cad" in result.required


def test_alias_no_dupes():
    description = """Required:
     Experience with FEA and Finite Element Analysis
     """

    result = extract_skills(description=description)
    assert result.required.count("finite element analysis") == 1


def test_extract_bachelors():
    text = "Requires a bachelor's degree in engineering."

    result = extract_education(text)

    assert result == ["bachelor"]


def test_extract_master_alias():
    text = "Requires an M.S. degree."

    result = extract_education(text)

    assert result == ["master"]


def test_extract_multiple_levels():
    text = "Bachelor's required. Master's preferred."

    result = extract_education(text)

    assert result == ["bachelor", "master"]


def test_extract_salary_range():
    result = extract_salary("The annual salary range is $90k-$110,000.")

    assert result == SalaryRange(minimum=90_000, maximum=110_000)


def test_extract_single_salary():
    result = extract_salary("Compensation starts at $125,000 annually.")

    assert result == SalaryRange(minimum=125_000, maximum=125_000)


def test_extract_salary_returns_none_when_missing():
    assert extract_salary("Competitive compensation.") is None
