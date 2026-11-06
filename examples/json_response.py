"""Call the featured endpoint and print the JSON result."""

import json
import os

from chartquery import ChartQueryClient

with ChartQueryClient(os.environ["CHARTQUERY_API_KEY"]) as client:
    response = client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18")
    print(json.dumps(response.data, indent=2))
