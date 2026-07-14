from job_intelligence.models import CandidateProfile, JobPosting, MatchResult
from job_intelligence.normalization import normalize_skill
def match_candidate(
        candidate: CandidateProfile,
        job: JobPosting
) -> MatchResult:
    """
    Match a candidate profile against a job posting and return a match result.
    
    Args:
        candidate (CandidateProfile): The candidate's profile.
        job (JobPosting): The job posting to match against.
        
    Returns:
        MatchResult: The result of the matching process, including score and skill matches.
    """
    candidate_skills = {
        normalize_skill(skill)
        for skill in candidate.skills
    }

    job_skills = {
        normalize_skill(skill)
        for skill in job.extracted_skills.required
    }

    preferred_job_skills = {
        normalize_skill(skill)
        for skill in job.extracted_skills.preferred
    }


    matched_skills = list(candidate_skills & job_skills)
    preferred_matched_skills = list(candidate_skills & preferred_job_skills)
    missing_skills = list(job_skills - candidate_skills)
    
    # Calculate a simple match score based on the number of matched skills
    score = len(matched_skills) / len(job.extracted_skills.required) if job.extracted_skills.required else 1
    
    return MatchResult(score=score, matched_skills=matched_skills, missing_skills=missing_skills, preferred_matched_skills=preferred_matched_skills)