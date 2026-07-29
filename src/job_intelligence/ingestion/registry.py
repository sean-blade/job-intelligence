from collections.abc import Callable

from job_intelligence.ingestion.base import JobConnector
from job_intelligence.ingestion.greenhouse_connector import GreenhouseConnector
from job_intelligence.ingestion.csv_connector import CSVConnector

CONNECTORS: dict[str, Callable[..., JobConnector]] = {
    "greenhouse": GreenhouseConnector,
    "csv": CSVConnector,
}


def get_connector(source: str, **kwargs) -> JobConnector:

    try:
        connector = CONNECTORS[source]
    except KeyError:
        raise ValueError(f"Unknown connector: {source}")

    return connector(**kwargs)
