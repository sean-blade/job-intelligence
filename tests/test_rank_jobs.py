from job_intelligence.rank_jobs import rank_jobs
from job_intelligence.models import CandidateProfile, JobPosting


def test_rank_jobs():
    candidate = CandidateProfile(skills=["Python", "SQL", "Machine Learning"])
    jobs = [
        JobPosting(
            title="Data Scientist",
            company="Tech Corp",
            skills=["Python", "SQL", "Statistics"],
        ),
        JobPosting(
            title="Software Engineer",
            company="Dev Inc",
            skills=["Python", "Java", "Design Patterns"],
        ),
    ]

    results = rank_jobs(candidate, jobs)

    assert results[0][1].score >= results[1][1].score
