import argparse
from pathlib import Path
from .analysis import categorize_prevalance, skill_prevalence
from .candidate_loader import load_candidate
from .ingestion.registry import get_connector
from .loader import load_jobs_from_csv, save_jobs_to_json
from .rank_jobs import rank_jobs
from .report import format_match_report, format_skill_report


def analyze_file(filepath: str):
    """Return skill prevalence statistics for jobs in a CSV file."""
    return skill_prevalence(load_jobs_from_csv(filepath))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze job postings")
    subparsers = parser.add_subparsers(dest="command")

    match_parser = subparsers.add_parser(
        "match", help="Match a candidate profile against job postings"
    )
    analyze_parser = subparsers.add_parser("analyze", help="Analyze job posting trends")
    ingest_parser = subparsers.add_parser(
        "ingest", help="Fetch jobs from external source"
    )

    ingest_parser.add_argument("source", choices=["csv", "greenhouse"])
    ingest_parser.add_argument("target")
    ingest_parser.add_argument(
        "--output",
        help="Optional path to save fetched jobs as JSON",
        default=None,
    )
    ingest_parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional limit on how many jobs to save",
    )
    analyze_parser.add_argument("filepath", help="Path to job CSV file")
    match_parser.add_argument(
        "--candidate", default=None, help="Path to candidate JSON file"
    )
    match_parser.add_argument("job_file", help="Path to job CSV file")

    return parser


def run_analyze(filepath: str) -> None:
    jobs = load_jobs_from_csv(filepath)
    skills = skill_prevalence(jobs)
    categories = categorize_prevalance(jobs)

    print(format_skill_report(skills))
    print("\nTop Categories")
    print("--------------------")
    for category, prevalence in categories.items():
        print(f"Category: {category}: {prevalence:.2%}")


def run_match(job_file: str, candidate_path: str | None) -> None:
    candidate = load_candidate(Path(candidate_path) if candidate_path else None)
    jobs = load_jobs_from_csv(job_file)
    print(format_match_report(rank_jobs(candidate, jobs)))


def run_ingest(source: str, target: str, output: str | None, limit: int | None) -> None:
    connector_options = {
        "csv": {"path": target},
        "greenhouse": {"board": target},
    }
    connector = get_connector(source, **connector_options[source])
    jobs = connector.fetch_jobs()
    print(f"Fetched: {len(jobs)} jobs from {source}")

    if output:
        jobs_to_save = jobs if limit is None else jobs[:limit]
        save_jobs_to_json(jobs_to_save, Path(output))
        print(f"Saved {len(jobs_to_save)} jobs to {output}")


def main() -> None:
    args = build_parser().parse_args()

    if args.command == "analyze":
        run_analyze(args.filepath)

    elif args.command == "match":
        run_match(args.job_file, args.candidate)

    elif args.command == "ingest":
        run_ingest(args.source, args.target, args.output, args.limit)
