import argparse

from .analysis import skill_frequency
from .loader import load_jobs_from_csv

def analyze_file(filepath: str):
    jobs = load_jobs_from_csv(filepath)

    return skill_frequency(jobs)

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

        skills = skill_frequency(jobs)

        print("\nTop Skills")
        print("-" * 20)

        for skill, count in sorted(
            skills.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(f"{skill}: {count}")