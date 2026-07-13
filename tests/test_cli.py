from job_intelligence.cli import analyze_file


def test_analyze_file():

    result = analyze_file("data/sample_jobs.csv")

    assert result["python"] == 2 / 3
    assert "cad" in result