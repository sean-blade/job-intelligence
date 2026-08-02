from job_intelligence.models import ExtractedSkills, JobPosting, SalaryRange
from job_intelligence.storage.sqlite_store import SQLiteStore


def test_sqlite_preserves_relevant_flag(tmp_path):
    db_path = tmp_path / "test_jobs.db"
    store = SQLiteStore(db_path)
    job = JobPosting(
        title="Job 1",
        company="Company A",
        location="Location X",
        description="Description 1",
        relevant=True,
    )
    store.save_jobs([job])
    loaded_jobs = store.load_jobs()
    store.close()

    assert len(loaded_jobs) == 1
    assert loaded_jobs[0].relevant is True


def test_sqlite_preserves_irrelevant_flag(tmp_path):
    db_path = tmp_path / "test_jobs.db"
    store = SQLiteStore(db_path)
    job = JobPosting(
        title="Job 2",
        company="Company B",
        location="Location Y",
        description="Description 2",
        relevant=False,
    )
    store.save_jobs([job])
    loaded_jobs = store.load_jobs()
    store.close()

    assert len(loaded_jobs) == 1
    assert loaded_jobs[0].relevant is False


def test_sqlite_preserves_complete_job_posting(tmp_path):
    db_path = tmp_path / "jobs.db"
    store = SQLiteStore(db_path)

    original_job = JobPosting(
        title="Biomedical Engineer",
        company="Example Corp",
        location="Remote",
        description="Python and CAD experience required.",
        relevant=True,
        salary=SalaryRange(minimum=90000, maximum=120000),
        education=["bachelor", "master"],
        extracted_skills=ExtractedSkills(
            required=["python", "cad"],
            preferred=["matlab"],
        ),
    )

    store.save_jobs([original_job])
    loaded_jobs = store.load_jobs()
    store.close()

    assert len(loaded_jobs) == 1

    loaded_job = loaded_jobs[0]

    assert loaded_job.title == original_job.title
    assert loaded_job.company == original_job.company
    assert loaded_job.location == original_job.location
    assert loaded_job.description == original_job.description
    assert loaded_job.relevant is True
    assert loaded_job.salary == original_job.salary
    assert loaded_job.education == original_job.education
    assert loaded_job.extracted_skills == original_job.extracted_skills


def test_sqlite_preserves_empty_optional_fields(tmp_path):
    store = SQLiteStore(tmp_path / "jobs.db")

    original_job = JobPosting(
        title="Engineer",
        salary=None,
        education=[],
        extracted_skills=ExtractedSkills(),
        relevant=False,
    )

    store.save_jobs([original_job])
    loaded_job = store.load_jobs()[0]
    store.close()

    assert loaded_job.salary is None
    assert loaded_job.education == []
    assert loaded_job.extracted_skills.required == []
    assert loaded_job.extracted_skills.preferred == []
    assert loaded_job.relevant is False
