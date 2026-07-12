from job_intelligence.analysis import skill_frequency
from job_intelligence.models import JobPosting


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