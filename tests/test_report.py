from job_intelligence.report import format_skill_report

def test_format_skill_report():
    skills = {
        "python": 0.75,
        "matlab": 0.25,
    }

    report = format_skill_report(skills)

    assert "python: 75%" in report
    assert "matlab: 25%" in report