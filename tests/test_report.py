from job_intelligence.report import format_skill_report, format_match_report
from job_intelligence.models import JobPosting, MatchResult

def test_format_skill_report():
    skills = {
        "python": 0.75,
        "matlab": 0.25,
    }

    report = format_skill_report(skills)

    assert "python: 75%" in report
    assert "matlab: 25%" in report

def test_format_match_report():
    job = JobPosting(
        title="Biomedical Engineer",
        company="MedTech Corp",
        location="Remote",
        description="Uses Python and MATLAB",
        skills=["python", "matlab"]
    )

    result = MatchResult(
        score=0.5,
        matched_skills=["python"],
        missing_skills=["matlab"]
    )

    matches = [
        (job, result)
    ]
    report = format_match_report(matches)

    assert "Biomedical Engineer" in report
    assert "Overall Match:" in report
    assert "Skill Match:" in report
    assert "Category Match:" in report
    assert "Matched Skills:" in report
    assert "Missing Skills:" in report
    assert "Matched Categories:" in report
    assert "Matched Skills:" in report
    assert "Missing Skills:" in report