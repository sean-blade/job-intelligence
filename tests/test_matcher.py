from job_intelligence.models import CandidateProfile, JobPosting, MatchResult
from job_intelligence.matcher import match_candidate

def test_match_candidate():
    # Create a temporary job posting
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        skills=["Python", "cad", "sql"]
    )

    # Create a temporary candidate profile
    candidate = CandidateProfile(
        name="Alice Bob",
        skills=["Python", "cad"],
        education=["B.Sc. in Biomedical Engineering"]
    )

    # Call the match_candidate function
    result = match_candidate(candidate, job)

    # Assert the match result
    assert result.score == 2 / 3  # 2 matched skills out of 3 required skills
    assert set(result.matched_skills) == {"Python", "cad"}
    assert set(result.missing_skills) == {"sql"}

def test_match_candidate_no_skills():
    # Create a temporary job posting with no required skills
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        skills=[]
    )

    # Create a temporary candidate profile
    candidate = CandidateProfile(
        name="Alice Bob",
        skills=["Python", "cad", "sql"],
        education=["B.Sc. in Biomedical Engineering"]
    )

    # Call the match_candidate function
    result = match_candidate(candidate, job)

    # Assert the match result
    assert result.score == 1  # No required skills, so score is 1
    assert set(result.matched_skills) == set()
    assert set(result.missing_skills) == set()

def test_perfect_match():
    # Create a temporary job posting
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        skills=["Python", "cad"]
    )

    # Create a temporary candidate profile with all required skills
    candidate = CandidateProfile(
        name="Alice Bob",
        skills=["Python", "cad"],
        education=["B.Sc. in Biomedical Engineering"]
    )

    # Call the match_candidate function
    result = match_candidate(candidate, job)

    # Assert the match result
    assert result.score == 1  # All required skills matched
    assert set(result.matched_skills) == {"Python", "cad"}
    assert set(result.missing_skills) == set()

def test_no_match():
    # Create a temporary job posting
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        skills=["Python", "cad"]
    )

    # Create a temporary candidate profile with no matching skills
    candidate = CandidateProfile(
        name="Alice Bob",
        skills=["Java", "C++"],
        education=["B.Sc. in Biomedical Engineering"]
    )

    # Call the match_candidate function
    result = match_candidate(candidate, job)

    # Assert the match result
    assert result.score == 0  # No required skills matched
    assert set(result.matched_skills) == set()
    assert set(result.missing_skills) == {"Python", "cad"}