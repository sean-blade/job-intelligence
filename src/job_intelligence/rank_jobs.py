from .models import CandidateProfile, JobPosting, MatchResult
from .matcher import match_candidate


def rank_jobs(
    candidate: CandidateProfile, jobs: list[JobPosting]
) -> list[tuple[JobPosting, MatchResult]]:
    """
    Match a candidate against multiple jobs and return results
    sorted by score descending.
    """

    matches = []

    for job in jobs:
        result = match_candidate(candidate, job)
        matches.append((job, result))

    matches.sort(key=lambda match: match[1].score, reverse=True)

    return matches
