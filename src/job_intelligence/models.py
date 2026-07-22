from dataclasses import dataclass, field


@dataclass
class ExtractedSkills:
    required: list[str] = field(default_factory=list)
    preferred: list[str] = field(default_factory=list)


@dataclass
class JobPosting:
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    extracted_skills: ExtractedSkills = field(default_factory=ExtractedSkills)
    skills: list[str] = field(default_factory=list)
    salary: str | None = None
    education: str | None = None

    def __post_init__(self):
        # If a flat `skills` list is provided (tests/legacy callers),
        # populate `extracted_skills.required` so both APIs work.
        if self.skills:
            self.extracted_skills.required = self.skills


@dataclass
class CandidateProfile:
    name: str | None = None
    skills: list[str] = field(default_factory=list)
    # experience: str | None = None
    education: list[str] = field(default_factory=list)


@dataclass
class MatchResult:
    score: float
    missing_required_skills: list[str] = field(default_factory=list)
    missing_preferred_skills: list[str] = field(default_factory=list)
    preferred_matched_skills: list[str] = field(default_factory=list)
    required_matched_skills: list[str] = field(default_factory=list)
    matched_categories: set[str] = field(default_factory=set)
    preferred_score: float = 0.0
    category_score: float = 0.0
    skill_score: float = 0.0
    education_match: bool = False
