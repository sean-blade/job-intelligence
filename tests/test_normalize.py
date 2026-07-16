from job_intelligence.normalization import normalize_skill, skill_in_text
from job_intelligence.models import CandidateProfile, JobPosting
from job_intelligence.matcher import match_candidate


def test_normalize_skill():
    assert normalize_skill(" Python ") == "python"
    assert normalize_skill("MATLAB") == "matlab"

def test_match_is_case_insensitive():
    job = JobPosting(
        title="Engineer",
        company="Test",
        location="Remote",
        description="",
        skills=["Python"]
    )

    candidate = CandidateProfile(
        name="Alice",
        skills=["python"]
    )

    result = match_candidate(candidate, job)

    assert result.score == 1

def test_skill_aliases(tmp_path):
    aliases_file = tmp_path / "aliases.json"

    aliases_file.write_text(
        # '{"fea": "finite element analysis"}',
        '{"finite element analysis": ["fea", "fem", "finite element method"]}',
        encoding="utf-8"
    )

    assert (
        normalize_skill("FEA", aliases_file)
        == "finite element analysis"
    )


def test_existing_skill_aliases():
    assert normalize_skill("FEA") == "finite element analysis"
    assert normalize_skill("FEM") == "finite element analysis"
    assert normalize_skill("computer-aided design") == "cad"
    assert normalize_skill("C.A.D.") == "cad"


def test_normalization_case_and_whitespace():
    assert normalize_skill("  FEA  ") == "finite element analysis"
    assert normalize_skill("CAD") == "cad"

def test_skill_match_exact():
    assert skill_in_text("python", "Experience with python")

def test_skill_match_case_insensitive():
    assert skill_in_text("python", "Experience with PYTHON")

def test_skill_nomatch_substring():
    assert not skill_in_text("cad", "Dedicated engineer")