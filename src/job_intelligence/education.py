from job_intelligence.models import CandidateProfile, JobPosting

EDUCATION_LEVELS = {
    "bachelor": 1,
    "master": 2,
    "phd": 3,
}


def highest_education_level(education: list[str]) -> str | None:
    if not education:
        return None

    return max(education, key=lambda edu: EDUCATION_LEVELS.get(edu, 0))


def education_match(candidate: CandidateProfile, job: JobPosting) -> bool:
    # Job has no required education
    if not job.education:
        return True
    #  Candidate has no education listed
    if not candidate.education:
        return False

    required_level = highest_education_level(job.education)
    candidate_level = highest_education_level(candidate.education)

    if required_level is None or candidate_level is None:
        return False

    return EDUCATION_LEVELS[candidate_level] >= EDUCATION_LEVELS[required_level]
