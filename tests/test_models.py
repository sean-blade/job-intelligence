from job_intelligence.models import JobPosting


def test_job_posting_creation():
    job = JobPosting(
        title="Biomedical Engineer",
        company="Example Corp",
        location="Remote",
        description="Develop medical devices"
    )

    assert job.title == "Biomedical Engineer"
    assert job.company == "Example Corp"

def test_job_posting_defaults():
    job = JobPosting(
        title="Research Engineer",
        company="Example Corp",
        location="Boston",
        description="Biomechanics research"
    )

    assert job.skills == []
    assert job.salary is None