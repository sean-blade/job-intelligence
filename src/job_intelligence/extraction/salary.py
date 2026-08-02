from job_intelligence.models import SalaryRange


def salary_overlap(
    candidate_salary: SalaryRange,
    job_salary: SalaryRange,
) -> bool:
    """Return whether the candidate and job salary ranges share an amount.

    A missing minimum means no lower bound; a missing maximum means no upper
    bound. This lets a candidate express a preference such as "$100k and up".
    """
    candidate_minimum = candidate_salary.minimum
    candidate_maximum = candidate_salary.maximum
    job_minimum = job_salary.minimum
    job_maximum = job_salary.maximum

    if candidate_minimum is not None and job_maximum is not None:
        if candidate_minimum > job_maximum:
            return False

    if candidate_maximum is not None and job_minimum is not None:
        if candidate_maximum < job_minimum:
            return False

    return True
