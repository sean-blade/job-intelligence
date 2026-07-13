import argparse

from .analysis import skill_prevalence
from .loader import load_jobs_from_csv
from .report import format_skill_report

def analyze_file(filepath: str):
    jobs = load_jobs_from_csv(filepath)

    return skill_prevalence(jobs)

def main():
    parser = argparse.ArgumentParser(
        description="Analyze job postings"
    )

    parser.add_argument(
        "command",
        choices=["analyze"],
        help="Command to run"
    )

    parser.add_argument(
        "filepath",
        help="Path to job CSV file"
    )

    args = parser.parse_args()

    if args.command == "analyze":
        jobs = load_jobs_from_csv(args.filepath)

        skills = skill_prevalence(jobs)

        print(format_skill_report(skills))