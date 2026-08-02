from job_intelligence.models import JobPosting
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
