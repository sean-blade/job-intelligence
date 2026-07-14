from pathlib import Path

from job_intelligence.loader import load_jobs_from_csv


def test_load_jobs_from_csv():

    filepath = Path("data/sample_jobs.csv")

    jobs = load_jobs_from_csv(filepath)

    assert len(jobs) == 3

    assert jobs[0].title == "Biomedical Engineer"

    assert "python" in jobs[0].extracted_skills.required