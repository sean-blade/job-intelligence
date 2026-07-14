def format_skill_report(skill_data: dict[str, float]) -> str:
    """
    Format skill prevalence data into a readable report.
    """
    lines = []

    lines.append("Top Skills")
    lines.append("-" * 20)

    for skill, prevalence in sorted(
        skill_data.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        lines.append(f"{skill}: {prevalence:.0%}")

    return "\n".join(lines)

def format_match_report(matches):
    lines = []

    for rank, (job, result) in enumerate(matches, start=1):
        lines.append(f"{rank}. {job.title} at {job.company}")
        lines.append(f"Match Score: {result.score:.0%}")

        matched = (
            ", ".join(result.matched_skills)
            if result.matched_skills
            else "None"
        )

        missing = (
            ", ".join(result.missing_skills)
            if result.missing_skills
            else "None"
        )

        lines.append(f"Matched Skills: {matched}")
        lines.append(f"Missing Skills: {missing}")
        lines.append("-" * 40)

    return "\n".join(lines)