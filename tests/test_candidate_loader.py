from job_intelligence.candidate_loader import load_candidate

def test_candidate_loader(tmp_path):

    candidate_file = tmp_path / "candidate.json"
    candidate_file.write_text(
        """
        {
            "name": "Alice Bob",
            "skills": ["Python", "cad"],
            "education": ["B.Sc. in Biomedical Engineering"]
        }
        """,
        encoding="utf-8"
    )

    candidate = load_candidate(candidate_file)

    assert candidate.name == "Alice Bob"
    assert "python" in candidate.skills