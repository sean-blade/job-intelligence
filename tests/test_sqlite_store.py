import time
from job_intelligence.models import ExtractedSkills, JobPosting, SalaryRange
from job_intelligence.storage.sqlite_store import SQLiteStore


def test_sqlite_preserves_relevant_flag(tmp_path):
    db_path = tmp_path / "test_jobs.db"
    store = SQLiteStore(db_path)
    job = JobPosting(
        url="https://example.com/job1",
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
        url="https://example.com/job1",
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
        url="https://example.com/job1",
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
        url="https://example.com/job1",
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


def test_save_new_job_inserts_row(tmp_path):
    db_path = tmp_path / "jobs.db"
    store = SQLiteStore(db_path)

    job = JobPosting(
        url="https://example.com/job1",
        title="Data Scientist",
        company="Example",
        location="Remote",
        description="Python required",
    )

    store.save_jobs([job])

    jobs = store.load_jobs()

    assert len(jobs) == 1


def test_duplicate_url_updates_existing_job(tmp_path):
    db_path = tmp_path / "jobs.db"
    store = SQLiteStore(db_path=db_path)

    original = JobPosting(
        url="https://example.com/job1",
        title="Data Scientist",
        company="Example",
        location="Remote",
        description="Old description",
    )

    updated = JobPosting(
        url="https://example.com/job1",
        title="Senior Data Scientist",
        company="Example",
        location="Remote",
        description="New description",
    )

    store.save_jobs([original])
    store.save_jobs([updated])

    jobs = store.load_jobs()

    assert len(jobs) == 1
    assert jobs[0].title == "Senior Data Scientist"


def test_different_urls_are_saved(tmp_path):
    db_path = tmp_path / "jobs.db"
    store = SQLiteStore(db_path=db_path)

    store.save_jobs(
        [
            JobPosting(url="https://example.com/1"),
            JobPosting(url="https://example.com/2"),
        ]
    )

    jobs = store.load_jobs()

    assert len(jobs) == 2


def test_first_seen_preserved_on_update(tmp_path):
    db_path = tmp_path / "jobs.db"
    store = SQLiteStore(db_path)

    job = JobPosting(
        url="https://example.com/job1",
        title="Data Scientist",
        company="Example",
        location="Remote",
        description="Original",
    )

    store.save_jobs([job])

    store.cursor.execute(
        "SELECT first_seen FROM jobs WHERE url = ?",
        (job.url,),
    )

    original_first_seen = store.cursor.fetchone()[0]

    updated_job = JobPosting(
        url="https://example.com/job1",
        title="Senior Data Scientist",
        company="Example",
        location="Remote",
        description="Updated",
    )

    store.save_jobs([updated_job])

    store.cursor.execute(
        "SELECT first_seen FROM jobs WHERE url = ?",
        (job.url,),
    )

    updated_first_seen = store.cursor.fetchone()[0]

    assert original_first_seen == updated_first_seen


def test_last_seen_is_updated_on_conflict(tmp_path):
    db_path = tmp_path / "jobs.db"
    store = SQLiteStore(db_path)

    job = JobPosting(
        url="https://example.com/job1",
        title="Data Scientist",
        company="Example",
        location="Remote",
        description="Original",
    )

    store.save_jobs([job])

    store.cursor.execute(
        "SELECT last_seen FROM jobs WHERE url = ?",
        (job.url,),
    )
    original_last_seen = store.cursor.fetchone()[0]

    time.sleep(1)

    updated_job = JobPosting(
        url="https://example.com/job1",
        title="Senior Data Scientist",
        company="Example",
        location="Remote",
        description="Updated",
    )

    store.save_jobs([updated_job])

    store.cursor.execute(
        "SELECT last_seen FROM jobs WHERE url = ?",
        (job.url,),
    )
    updated_last_seen = store.cursor.fetchone()[0]

    assert updated_last_seen > original_last_seen


def get_job_timestamps(store, url):
    store.cursor.execute(
        "SELECT first_seen, last_seen FROM jobs WHERE url = ?",
        (url,),
    )
    return store.cursor.fetchone()
