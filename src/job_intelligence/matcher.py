from job_intelligence.models import CandidateProfile, JobPosting, MatchResult

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
    matched_skills = list(set(candidate.skills) & set(job.skills))
    missing_skills = list(set(job.skills) - set(candidate.skills))
    
    # Calculate a simple match score based on the number of matched skills
    score = len(matched_skills) / len(job.skills) if job.skills else 1
    
    return MatchResult(score=score, matched_skills=matched_skills, missing_skills=missing_skills)