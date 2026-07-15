from job_intelligence.report import format_skill_report, format_match_report
from job_intelligence.models import JobPosting, MatchResult
from job_intelligence.parser import ExtractedSkills

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
        extracted_skills=ExtractedSkills(
            required=["python", "matlab"]
        )
    )

    result = MatchResult(
        score=0.5,
        skill_score=0.5,
        category_score=0.0,
        required_matched_skills=["python"],
        preferred_matched_skills=["cad"],
        missing_required_skills=["matlab"],
        missing_preferred_skills=["docker"],
        matched_categories={"programming"}
    )

    matches = [
        (job, result)
    ]
    report = format_match_report(matches)

    assert "Biomedical Engineer" in report
    assert "Overall Match:" in report
    assert "Skill Match:" in report
    assert "Category Match:" in report
    assert "Matched Required Skills" in report
    assert "Matched Preferred Skills" in report
    assert "Missing Required Skills" in report
    assert "Missing Preferred Skills" in report
    assert "python" in report
    assert "matlab" in report
    assert "cad" in report
    assert "docker" in report
    assert "programming" in report