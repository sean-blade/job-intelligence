from job_intelligence.category import load_categories

def test_load_categories():
    categories = load_categories()
    assert "programming" in categories
    assert "python" in categories["programming"]