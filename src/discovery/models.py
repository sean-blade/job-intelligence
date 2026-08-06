from dataclasses import dataclass


@dataclass
class OpportunityTarget:
    company_name: str | None = None
    ats_type: str | None = None
    slug: str | None = None
    industry: str | None = None
    score: float = 0
    active: bool = False
