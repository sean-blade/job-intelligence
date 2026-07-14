from job_intelligence.analysis import skill_frequency, skill_prevalence
from job_intelligence.models import JobPosting, ExtractedSkills


def test_skill_frequency():

    jobs = [
        JobPosting(
            title="Engineer",
            company="Company A",
            location="Remote",
            description="",
            skills=["python", "matlab"],
        ),
        JobPosting(
            title="Analyst",
            company="Company B",
            location="Remote",
            description="",
            skills=["python", "sql"],
        ),
    ]

    result = skill_frequency(jobs)

    assert result["python"] == 2
    assert result["matlab"] == 1
    assert result["sql"] == 1

def test_skill_prevalence():
    jobs = [
        JobPosting(
            title="Engineer",
            company="Company A",
            location="Remote",
            description="",
            extracted_skills=ExtractedSkills(required=["python", "matlab"]),
        ),
        JobPosting(
            title="Analyst",
            company="Company B",
            location="Remote",
            description="",
            extracted_skills=ExtractedSkills(required=["python", "sql"]),
        ),
    ]

    result = skill_prevalence(jobs)

    assert result["python"] == 1.0
    assert result["matlab"] == 0.5
    assert result["sql"] == 0.5