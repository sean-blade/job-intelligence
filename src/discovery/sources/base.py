from abc import ABC, abstractmethod

from discovery.models import OpportunityTarget


class DiscoverySource(ABC):

    @abstractmethod
    def discover(self) -> OpportunityTarget:
        """Return discoverd companies."""
        pass
