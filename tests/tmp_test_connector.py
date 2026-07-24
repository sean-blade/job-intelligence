from job_intelligence.ingestion.greenhouse_connector import GreenhouseConnector

connector = GreenhouseConnector("stripe")
jobs = connector.fetch_jobs()

print(f"Found {len(jobs)} jobs")

if jobs:
    print(jobs[0].title)
    print(jobs[0].location)
