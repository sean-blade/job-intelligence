import truststore
from job_intelligence.ingestion.greenhouse_connector import (
    GreenhouseConnector,
)

truststore.inject_into_ssl()


connector = GreenhouseConnector("stripe")

jobs = connector.fetch_jobs()

print(f"Found {len(jobs)} jobs")

if jobs:
    print(jobs[0])
