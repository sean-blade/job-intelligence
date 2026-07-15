from job_intelligence.scoring import calculate_category_score


def test_category_score():
    candidate = ["programming", "engineering"]
    job = ["engineering","data science"]
    
    result = calculate_category_score(candidate, job)

    assert result == 0.5


def test_no_job_categories():
    
    result = calculate_category_score(
        ["engineering"],
        []
    )

    assert result == 1.0