import csv
import json
from pathlib import Path

from job_intelligence.loader import load_jobs_from_csv


def test_load_jobs_from_csv():

    filepath = Path("data/sample_jobs.csv")

    jobs = load_jobs_from_csv(filepath)

    assert len(jobs) == 3

    assert jobs[0].title == "Biomedical Engineer"

    assert "python" in jobs[0].extracted_skills.required


def test_save_first_ten_jobs_to_json(tmp_path):
    csv_path = tmp_path / "jobs.csv"
    json_path = tmp_path / "first_10_jobs.json"

    rows = [
        {
            "title": f"Engineer {i}",
            "company": "TestCo",
            "location": "Remote",
            "description": "Work with Python.",
        }
        for i in range(1, 13)
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["title", "company", "location", "description"]
        )
        writer.writeheader()
        writer.writerows(rows)

    jobs = load_jobs_from_csv(csv_path)
    first_ten = jobs[:10]

    from job_intelligence.loader import save_jobs_to_json

    save_jobs_to_json(first_ten, json_path)

    assert json_path.exists()

    saved = json.loads(json_path.read_text(encoding="utf-8"))
    assert isinstance(saved, list)
    assert len(saved) == 10
    assert saved[0]["title"] == "Engineer 1"
    assert saved[-1]["title"] == "Engineer 10"
