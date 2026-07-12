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