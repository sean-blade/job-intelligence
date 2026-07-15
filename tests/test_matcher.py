from job_intelligence.models import CandidateProfile, ExtractedSkills, JobPosting, MatchResult
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
    assert result.skill_score == 2 / 3
    assert result.category_score == 1.0
    assert result.score == 0.7666666666666666
    assert set(result.required_matched_skills) == {"python", "cad"}
    assert set(result.missing_required_skills) == {"sql"}
    assert "programming" in result.matched_categories


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
    assert set(result.required_matched_skills) == set()
    assert set(result.missing_required_skills) == set()


def test_perfect_match():
    # Create a temporary job posting
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        extracted_skills=ExtractedSkills(required=["python", "cad"])
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
    assert result.score == 1 # All required skills matched
    assert set(result.required_matched_skills) == {"python", "cad"}
    assert set(result.missing_required_skills) == set()
    assert result.category_score == 1.0


def test_partial_category_match():
    # Create a temporary job posting
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        extracted_skills=ExtractedSkills(required=["python", "cad"])
    )

    # Create a temporary candidate profile with all required skills
    candidate = CandidateProfile(
        name="Alice Bob",
        skills=["Python"],
        education=["B.Sc. in Biomedical Engineering"]
    )

    # Call the match_candidate function
    result = match_candidate(candidate, job)

    assert result.category_score == 0.5


def test_no_match():
    # Create a temporary job posting
    job = JobPosting(
        title="Engineer",
        company="Tech Corp",
        location="Zimbabwe",
        description="Develop software applications",
        extracted_skills=ExtractedSkills(required=["Python", "cad"])
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
    assert result.skill_score == 0
    assert result.category_score > 0 
    assert result.score > 0
    assert set(result.required_matched_skills) == set()
    assert set(result.preferred_matched_skills) == set()
    assert set(result.missing_preferred_skills) == set()
    assert set(result.missing_required_skills) == {"python", "cad"}


def test_category_only_match():

    job = JobPosting(
        title="Software Engineer",
        company="Tech Corp",
        extracted_skills=ExtractedSkills(
            required=["python"]
        )
    )

    candidate = CandidateProfile(
        name="Alice",
        skills=["sql"]
    )

    result = match_candidate(candidate, job)

    assert result.skill_score == 0
    assert result.category_score == 1.0


def test_preferred_skill_match():

    job = JobPosting(
        title="Engineer",
        company="Company",
        extracted_skills=ExtractedSkills(
            required=["python"],
            preferred=["cad"]
        )
    )

    candidate = CandidateProfile(
        name="Alice",
        skills=["python", "cad"]
    )

    result = match_candidate(candidate, job)

    assert result.required_matched_skills == ["python"]
    assert result.preferred_matched_skills == ["cad"]


def test_missing_preferred_skill():

    job = JobPosting(
        title="Engineer",
        company="Company",
        extracted_skills=ExtractedSkills(
            required=["python"],
            preferred=["cad"]
        )
    )

    candidate = CandidateProfile(
        name="Alice",
        skills=["python"]
    )

    result = match_candidate(candidate, job)

    assert result.skill_score == 1.0
    assert result.preferred_matched_skills == []


def test_preferred_skill_does_not_replace_required():
    job = JobPosting(
        title="Engineer",
        company="Company",
        extracted_skills=ExtractedSkills(
            required=["python", "matlab"],
            preferred=["cad"]
        )
    )

    candidate = CandidateProfile(
        name="Alice",
        skills=["python", "cad"]
    )

    result = match_candidate(candidate, job)

    assert result.missing_required_skills == ["matlab"]
    assert result.skill_score == 0.5


def test_missing_skills():
    job = JobPosting(
        title="Engineer",
        company="Company",
        extracted_skills=ExtractedSkills(
            required=["python", "matlab"],
            preferred=["cad"]
        )
    )

    candidate = CandidateProfile(
        name="Alice",
        skills=["python"]
    )

    result = match_candidate(candidate, job)
    assert set(result.missing_required_skills) == {"matlab"}
    assert set(result.missing_preferred_skills) == {"cad"}