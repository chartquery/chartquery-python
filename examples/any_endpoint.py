"""Call any path with request() and handle API errors."""

from chartquery import ChartQueryAPIError, ChartQueryClient, JsonResponse

with ChartQueryClient() as client:  # reads CHARTQUERY_API_KEY
    try:
        response = client.request("GET", "/v1/usage")
        if isinstance(response, JsonResponse):
            print(response.data)
    except ChartQueryAPIError as error:
        print(f"HTTP {error.status}: {error}")
