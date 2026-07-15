from job_intelligence.models import CandidateProfile, JobPosting, MatchResult
from job_intelligence.normalization import normalize_skill
from job_intelligence.category import categorize_skill
from job_intelligence.scoring import calculate_category_score


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
    matched_categories = set()


    for skill in matched_skills:
        category = categorize_skill(skill)

        if category:
            matched_categories.add(category)

    candidate_categories = set()

    for skill in candidate.skills:
        category = categorize_skill(skill)

        if category:
            candidate_categories.add(category)


    job_categories = set()

    for skill in job.extracted_skills.required:
        category = categorize_skill(skill)

        if category:
            job_categories.add(category)


    category_score = calculate_category_score(
        list(candidate_categories),
        list(job_categories)
    )
    
    # Calculate a simple match score based on the number of matched skills
    skill_score = len(matched_skills) / len(job.extracted_skills.required) if job.extracted_skills.required else 1

    score = 0.7 * skill_score + 0.3 * category_score

    return MatchResult(score=score, matched_skills=matched_skills, missing_skills=missing_skills, preferred_matched_skills=preferred_matched_skills, matched_categories=matched_categories, category_score=category_score, skill_score=skill_score)