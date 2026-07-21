import argparse

from job_intelligence.rank_jobs import rank_jobs

from .analysis import skill_prevalence, categorize_prevalance
from .loader import load_jobs_from_csv
from .report import format_skill_report, format_match_report
from .candidate_loader import load_candidate


def analyze_file(filepath: str):
    jobs = load_jobs_from_csv(filepath)

    return skill_prevalence(jobs)


def main():
    parser = argparse.ArgumentParser(description="Analyze job postings")

    subparsers = parser.add_subparsers(dest="command")
    match_parser = subparsers.add_parser("match")
    analyze_parser = subparsers.add_parser("analyze")

    analyze_parser.add_argument("filepath", help="Path to job CSV file")

    match_parser.add_argument(
        "--candidate", default=None, help="Path to candidate JSON file"
    )

    match_parser.add_argument("job_file", help="Path to job CSV file")

    args = parser.parse_args()

    if args.command == "analyze":
        jobs = load_jobs_from_csv(args.filepath)

        skills = skill_prevalence(jobs)
        categories = categorize_prevalance(jobs)

        print(format_skill_report(skills))
        print("\nTop Categories")
        print("--------------------")
        for category, prevalence in categories.items():
            print(f"Category: {category}: {prevalence:.2%}")

    elif args.command == "match":
        candidate = load_candidate(args.candidate)
        jobs = load_jobs_from_csv(args.job_file)
        matches = rank_jobs(candidate, jobs)
        print(format_match_report(matches))
