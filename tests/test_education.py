from job_intelligence.education import highest_education_level, education_match
from job_intelligence.models import CandidateProfile, JobPosting


def test_highest_edu():
    assert highest_education_level(["bachelor", "master"]) == "master"


def test_master_meets_bachelor_req():
    candidate = CandidateProfile(education=["master"])
    job = JobPosting(education=["bachelor"])

    assert education_match(candidate, job)
