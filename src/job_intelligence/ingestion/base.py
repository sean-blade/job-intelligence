from abc import ABC, abstractmethod

from job_intelligence.models import JobPosting


class JobConnector(ABC):
    """Base class for all job data sources"""

    def __init__(self, **kwargs):
        self.config = kwargs

    @property
    @abstractmethod
    def source_name(self) -> str:
        pass

    @abstractmethod
    def fetch_jobs(self) -> list[JobPosting]:
        """Return jobs in the internal format."""
        raise NotImplementedError
