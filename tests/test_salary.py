from job_intelligence.models import SalaryRange
from job_intelligence.salary import salary_overlap


def test_salary_ranges_overlap():
    candidate = SalaryRange(minimum=90_000, maximum=120_000)
    job = SalaryRange(minimum=110_000, maximum=140_000)

    assert salary_overlap(candidate, job) is True


def test_salary_ranges_do_not_overlap():
    candidate = SalaryRange(minimum=90_000, maximum=110_000)
    job = SalaryRange(minimum=120_000, maximum=140_000)

    assert salary_overlap(candidate, job) is False


def test_touching_salary_ranges_overlap():
    candidate = SalaryRange(minimum=90_000, maximum=110_000)
    job = SalaryRange(minimum=110_000, maximum=140_000)

    assert salary_overlap(candidate, job) is True


def test_salary_range_with_no_maximum_overlaps_higher_job_range():
    candidate = SalaryRange(minimum=100_000)
    job = SalaryRange(minimum=120_000, maximum=140_000)

    assert salary_overlap(candidate, job) is True
