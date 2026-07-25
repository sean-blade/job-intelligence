from job_intelligence.models import JobPosting
from job_intelligence.ingestion.csv_connector import CSVConnector
from job_intelligence.ingestion.base import JobConnector
from job_intelligence.ingestion.greenhouse_connector import GreenhouseConnector
from unittest.mock import Mock, patch
import requests
import pytest


def test_csv_connector_source_name():
    connector = CSVConnector("data/sample_jobs.csv")

    assert connector.source_name == "csv"


def test_csv_connector_loads_jobs():
    connector = CSVConnector("data/sample_jobs.csv")

    jobs = connector.fetch_jobs()

    assert len(jobs) > 0


def test_csv_connector_returns_job_postings():
    connector = CSVConnector("data/sample_jobs.csv")

    jobs = connector.fetch_jobs()

    assert all(isinstance(job, JobPosting) for job in jobs)


def test_csv_connector_is_job_connector():
    connector = CSVConnector("data/sample_jobs.csv")

    assert isinstance(connector, JobConnector)


def test_greenhouse_source_name():
    connector = GreenhouseConnector("stripe")

    assert connector.source_name == "greenhouse"


def test_greenhouse_stores_board():
    connector = GreenhouseConnector("stripe")

    assert connector.board == "stripe"


@patch("job_intelligence.ingestion.greenhouse_connector.requests.get")
def test_greenhouse_connector_returns_jobs(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "jobs": [
            {
                "title": "Software Engineer",
                "content": "Python experience required",
                "location": {"name": "Remote"},
            }
        ]
    }

    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    connector = GreenhouseConnector("stripe")
    jobs = connector.fetch_jobs()

    assert len(jobs) == 1
    assert jobs[0].title == "Software Engineer"
    assert jobs[0].company == "stripe"
    assert jobs[0].location == "Remote"
    assert jobs[0].description == "Python experience required"


@patch("job_intelligence.ingestion.greenhouse_connector.requests.get")
def test_greenhouse_connector_extracts_company_from_response(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "jobs": [
            {
                "title": "Software Engineer",
                "content": "Python experience required",
                "location": {"name": "Remote"},
                "company": {"name": "Stripe Inc."},
            }
        ]
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    connector = GreenhouseConnector("stripe")
    jobs = connector.fetch_jobs()

    assert len(jobs) == 1
    assert jobs[0].company == "Stripe Inc."


@patch("job_intelligence.ingestion.greenhouse_connector.requests.get")
def test_greenhouse_connector_cleans_html_description(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "jobs": [
            {
                "title": "Software Engineer",
                "content": "<p>Python <strong>experience</strong> required &amp; preferred</p>",
                "location": {"name": "Remote"},
            }
        ]
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    connector = GreenhouseConnector("stripe")
    jobs = connector.fetch_jobs()

    assert jobs[0].description == "Python experience required & preferred"


@patch("job_intelligence.ingestion.greenhouse_connector.requests.get")
def test_greenhouse_connector_uses_correct_url(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"jobs": []}
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    connector = GreenhouseConnector("stripe")
    connector.fetch_jobs()

    mock_get.assert_called_once_with(
        "https://boards-api.greenhouse.io/v1/boards/stripe/jobs?content=true",
        timeout=10,
    )


@patch("job_intelligence.ingestion.greenhouse_connector.requests.get")
def test_greenhouse_connector_handles_no_jobs(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {"jobs": []}

    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    connector = GreenhouseConnector("stripe")

    jobs = connector.fetch_jobs()

    assert jobs == []


@patch("job_intelligence.ingestion.greenhouse_connector.requests.get")
def test_greenhouse_connector_raises_on_failed_request(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError()

    mock_get.return_value = mock_response

    connector = GreenhouseConnector("stripe")

    with pytest.raises(requests.HTTPError):
        connector.fetch_jobs()
