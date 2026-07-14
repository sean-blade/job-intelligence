import argparse

from .analysis import skill_prevalence
from .loader import load_jobs_from_csv
from .report import format_skill_report
from .candidate_loader import load_candidate
from .matcher import match_candidate

def analyze_file(filepath: str):
    jobs = load_jobs_from_csv(filepath)

    return skill_prevalence(jobs)

def main():
    parser = argparse.ArgumentParser(
        description="Analyze job postings"
    )

    # parser.add_argument(
    #     "command",
    #     choices=["analyze"],
    #     help="Command to run"
    # )

    # parser.add_argument(
    #     "filepath",
    #     help="Path to job CSV file"
    # )

    subparsers = parser.add_subparsers(dest="command")
    match_parser = subparsers.add_parser("match")
    analyze_parser = subparsers.add_parser("analyze")

    analyze_parser.add_argument(
        "filepath",
        help="Path to job CSV file"
    )

    match_parser.add_argument(
        "candidate_file",
        help="Path to candidate JSON file"
    )

    match_parser.add_argument(
        "job_file",
        help="Path to job CSV file"
    )

    args = parser.parse_args()

    if args.command == "analyze":
        jobs = load_jobs_from_csv(args.filepath)

        skills = skill_prevalence(jobs)

        print(format_skill_report(skills))

    elif args.command == "match":
        candidate = load_candidate(args.candidate_file)
        jobs = load_jobs_from_csv(args.job_file)
        matches = []
        for job in jobs:
            result = match_candidate(candidate, job)
            matches.append((job, result))
            # print("-" * 40)

        matches.sort(key=lambda x: x[1].score, reverse=True)

        for job, result in matches:
            print(f"Job: {job.title} at {job.company}")
            print(f"Match Score: {result.score:.0%}")
            print(f"Matched Skills: {', '.join(result.matched_skills) if result.matched_skills else 'None'}")
            print(f"Missing Skills: {', '.join(result.missing_skills) if result.missing_skills else 'None'}")
            print()