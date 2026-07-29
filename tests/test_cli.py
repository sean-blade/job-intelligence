import sys
import subprocess
import json
from job_intelligence.cli import analyze_file


def test_analyze_file():

    result = analyze_file("data/sample_jobs.csv")

    assert result["python"] == 2 / 3
    assert result["cad"] == 1 / 3


def test_match_command():
    # Run the CLI command for matching
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "job_intelligence",
            "match",
            # "data/sample_candidate.json",
            "data/sample_jobs.csv",
        ],
        capture_output=True,
        text=True,
    )
    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)
    # Check that the command executed successfully
    assert result.returncode == 0

    # Check that the output contains expected match information
    output = result.stdout
    assert "Biomedical Engineer" in output
    assert "Overall Match:" in output
    assert "Skill Match:" in output
    assert "Category Match:" in output
    assert "Matched Required Skills" in output
    assert "Matched Preferred Skills" in output
    assert "Missing Required Skills" in output
    assert "Missing Preferred Skills" in output

    # TODO: rework job ranking checks, after switching out the skills.json file the order of these changed.
    # assert output.index("Data Analyst") < output.index("Mechanical Engineer")
    # assert output.index("Mechanical Engineer") < output.index("Biomedical Engineer")


def test_analyze_command_categories():

    result = subprocess.run(
        [sys.executable, "-m", "job_intelligence", "analyze", "data/sample_jobs.csv"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Top Categories" in result.stdout


def test_match_with_custom_candidate():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "job_intelligence",
            "match",
            "data/sample_jobs.csv",
            "--candidate",
            "tests/data/sample_candidate.json",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Overall Match" in result.stdout


def test_ingest_command_saves_json(tmp_path):
    output_path = tmp_path / "jobs.json"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "job_intelligence",
            "ingest",
            "csv",
            "data/sample_jobs.csv",
            "--output",
            str(output_path),
            "--limit",
            "2",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_path.exists()

    saved = json.loads(output_path.read_text(encoding="utf-8"))
    assert isinstance(saved, list)
    assert len(saved) == 2
    assert saved[0]["title"] == "Biomedical Engineer"
