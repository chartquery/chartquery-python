"""Start an async job and wait for its result."""

from chartquery import ChartQueryClient

with ChartQueryClient() as client:  # reads CHARTQUERY_API_KEY
    submitted = client.chart_ai(
        prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18", is_async=True
    )
    job = client.wait_for_job(
        submitted.data["job_id"],
        on_progress=lambda j: print(j["status"], j.get("progress")),
    )
    print(job.data)
