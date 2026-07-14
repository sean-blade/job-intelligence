from dataclasses import dataclass, field


@dataclass
class JobPosting:
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    skills: list[str] = field(default_factory=list)
    salary: str | None = None

@dataclass
class CandidateProfile:
    name: str | None = None
    skills: list[str] = field(default_factory=list)
    # experience: str | None = None
    education: list[str] = field(default_factory=list)
    
@dataclass
class MatchResult:
    score: float
    matched_skills: list[str] = field(default_factory=list)
    missing_skills: list[str] = field(default_factory=list)