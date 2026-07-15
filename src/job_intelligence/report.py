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

        lines.append(f"Overall Match: {result.score:.0%}")
        lines.append(f"Skill Match: {result.skill_score:.0%}")
        lines.append(f"Category Match: {result.category_score:.0%}")
        lines.append("")
        missing_required = (
            ", ".join(result.missing_required_skills)
            if result.missing_required_skills
            else "None"
        )        
        
        missing_preferred = (
            ", ".join(result.missing_preferred_skills)
            if result.missing_preferred_skills
            else "None"
        )

        categories = (
            ", ".join(sorted(result.matched_categories))
            if result.matched_categories
            else "None"
        )

        required = (
            ", ".join(result.required_matched_skills)
            if result.required_matched_skills
            else "None"
        )

        preferred= (
            ", ".join(result.preferred_matched_skills)
            if result.preferred_matched_skills
            else "None"
        )

        lines.append(f"Matched Required Skills: {required}")
        lines.append("")
        lines.append(f"Matched Preferred Skills: {preferred}")
        lines.append("")
        lines.append(f"Matched Categories: {categories}")
        lines.append("")
        lines.append(f"Missing Required Skills: {missing_required}")
        lines.append("")
        lines.append(f"Missing Preferred Skills: {missing_preferred}")
        lines.append("")
        

        lines.append("-" * 40)

    return "\n".join(lines)