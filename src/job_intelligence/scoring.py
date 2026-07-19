def calculate_category_score(
    candidate_categories: list[str], job_categories: list[str]
) -> float:
    """
    Calculate overlap between candidate and job categories.
    """
    if not job_categories:
        return 1.0

    matched = set(candidate_categories) & set(job_categories)

    return len(matched) / len(job_categories)
