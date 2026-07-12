from dataclasses import dataclass, field


@dataclass
class JobPosting:
    title: str
    company: str
    location: str
    description: str
    skills: list[str] = field(default_factory=list)
    salary: str | None = None