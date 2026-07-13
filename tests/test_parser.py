from job_intelligence.parser import extract_skills, parse_job_description


def test_extract_skills():
    description = """
    Looking for an engineer with Python,
    MATLAB, and finite element analysis experience.
    """

    skills = extract_skills(description)

    assert "python" in skills
    assert "matlab" in skills
    assert "finite element analysis" in skills


def test_parse_job_description():
    job = parse_job_description(
        title="Biomedical Engineer",
        company="Example Corp",
        location="Remote",
        description="Experience with Python and CAD."
    )

    assert job.title == "Biomedical Engineer"
    assert "python" in job.skills
    assert "cad" in job.skills

def test_custom_skill_file(tmp_path):
    # Create a temporary skills file
    skills_file = tmp_path / "skills.json"
    skills_file.write_text('["python", "docker"]', encoding="utf-8")

    description = "Looking for an engineer with Python and docker experience."
    result = extract_skills(description, skills_file=skills_file)

    assert result == ["python", "docker"]