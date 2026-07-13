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