# ChartQuery Python SDK

The official Python SDK for the [ChartQuery](https://www.chartquery.com) chart and QR code API.

Generate chart images, diagrams, barcodes, QR codes and thermal labels on demand. PNG, SVG or PDF output.

The SDK exposes **20 typed methods**, one per documented endpoint, with blocking and `asyncio` clients built on [HTTPX](https://www.python-httpx.org/), plus a generic `request()`.

## Requirements

- Python 3.11 or newer

## Installation

```sh
pip install chartquery
```

## Get your API key

[Sign up for ChartQuery](https://app.chartquery.com/register) or sign in, then copy your API key from the [dashboard](https://app.chartquery.com). The client reads the `CHARTQUERY_API_KEY` environment variable when no key is passed.

## Quick start

```python
import os

from chartquery import ChartQueryClient

with ChartQueryClient(os.environ["CHARTQUERY_API_KEY"]) as client:
    response = client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18")
    print(response.data)
```

Keyword arguments mirror the [API reference](https://app.chartquery.com/openapi). Python keywords get a trailing underscore (`from_=`), and the wire name is used on the request.

## Binary responses

Endpoints that can return a file (image, PDF…) return a `JsonResponse` or a `BinaryResponse`:

```python
from chartquery import BinaryResponse

response = client.qrcode(data="https://chartquery.com", format="png")
if isinstance(response, BinaryResponse):
    with open("qrcode.png", "wb") as file:
        file.write(response.bytes)
```

## Async jobs

Any call accepts `is_async: true` (useful past the 60-second server limit): the response is then a `job_id`. `wait_for_job()` polls `GET /v1/jobs/{id}` until the job reaches a terminal status (`CompletedJob`, `Error`, `NotFound`, `BadRequest`):

```python
submitted = client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18", is_async=True)
job = client.wait_for_job(
    submitted.data["job_id"],
    on_progress=lambda j: print(j["status"], j.get("progress")),
)
print(job.data)
```

## Async I/O

```python
import asyncio

from chartquery import AsyncChartQueryClient


async def main() -> None:
    async with AsyncChartQueryClient() as client:
        response = await client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18")
        print(response.data)


asyncio.run(main())
```

## GET or POST

Methods use GET when the endpoint supports it (parameters in the query string). POST sends the same parameters as a JSON body:

```python
from chartquery import RequestOptions

client.barcode(data="test", request_options=RequestOptions(method="POST"))
```

`None` values are omitted, `False` and `0` are sent, and sequences repeat the parameter name.

## Any endpoint

```python
response = client.request("GET", "/v1/usage")
```

## Errors

```python
from chartquery import ChartQueryAPIError

try:
    client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18")
except ChartQueryAPIError as error:
    print(error.status, error, error.response_body)
```

| Error | When |
| --- | --- |
| `ChartQueryConfigurationError` | Missing API key, invalid options, unsupported method, closed client. |
| `ChartQuerySerializationError` | A required parameter is missing or a value can't be sent. |
| `ChartQueryTransportError` | Network failure or timeout. |
| `ChartQueryAPIError` | Non-2xx status (`status`, `error_message`, `response_body`, `raw_response`). |
| `ChartQueryResponseDecodingError` | A success response could not be decoded. |

All of them extend `ChartQueryError`.

## Retries

Requests are retried up to 3 times after a network error, a `408`, `500`, `502`, `503` or `504`, or a rate limit — which the API returns as `401` (or `429`) with a `Rate limit exceeded` message. Per-key quota errors (`…: quota daily`) are not retried, nor are `400`, `402`, `404` or client-side timeouts. The delay starts at 1 second and grows 1.5× per retry (capped at 30 seconds); a `Retry-After` header wins.

```python
client = ChartQueryClient(max_retries=5, retry_delay=0.5)

# or for one request
client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18", request_options=RequestOptions(max_retries=0))
```

## Batch requests

`batch()` runs a function per item on 10 threads (`concurrency`) and returns one `BatchResult` per item, in input order. A failing item never stops the others. `AsyncChartQueryClient.batch()` does the same with `asyncio`.

```python
inputs = ["Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18", "Market share as a pie chart: A 40, B 35, C 25"]
results = client.batch(inputs, lambda prompt: client.chart_ai(prompt=prompt), concurrency=5)

for result in results:
    if result.ok:
        print(result.value.data)
    else:
        print(inputs[result.index], result.error)
```

| Constant | Default | Description |
| --- | --- | --- |
| `DEFAULT_CONCURRENCY` | `10` | Tasks run at the same time by batch |
| `DEFAULT_TIMEOUT` | `120.0` | Request timeout (seconds) |
| `MAX_RETRIES` | `3` | Retry attempts after a network error, a 408/5xx or a rate limit |
| `RETRY_BACKOFF_FACTOR` | `1.5` | Exponential backoff multiplier |
| `DEFAULT_RETRY_DELAY` | `1.0` | Delay before the first retry (seconds) |

## Timeouts and custom HTTPX clients

```python
import httpx

from chartquery import ChartQueryClient, RequestOptions

client = ChartQueryClient(timeout=60)  # seconds, default 120, None disables
client.chart_ai(prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18", request_options=RequestOptions(timeout=30))

# Bring your own HTTPX client (proxies, limits, event hooks…). You keep ownership of it.
http_client = httpx.Client(proxy="http://localhost:8080")
client = ChartQueryClient(http_client=http_client)
```

## Endpoints

20 methods, generated from the [OpenAPI document](https://app.chartquery.com/openapi).

| Method | HTTP | Description |
| --- | --- | --- |
| `barcode()` | GET / POST `/v1/barcode` | Generate a barcode image via GET. Output: SVG (default) or PNG. Supports 25+ formats: EAN-13, Code 128, ITF-14, GS1-128, postal codes and m… |
| `chart()` | GET / POST `/v1/chart` | Render a Chart.js image via GET. Pass the full chart object as URL-encoded JSON in query. Prefer format png for ChatGPT. POST sends the sam… |
| `chart_ai()` | GET / POST `/v1/chart/ai` | Describe a chart in plain English via GET and get a rendered image back. Powered by AI. |
| `chart_render()` | GET `/v1/chart/render/{id}` | Render a previously saved chart by ID. Public, no API key required. Supports URL overrides for templates (?data1=, ?labels=, ?title=…). |
| `chart_view()` | GET `/v1/chart/view/{id}` | View a previously saved chart as an interactive HTML page. Public, no API key required. Iframe-embeddable. |
| `diagram()` | GET / POST `/v1/diagram` | Render a diagram via GET. Use type (mermaid, d2, …), query (source code), and format=png for ChatGPT. POST uses diagram_type and diagram_so… |
| `diagram_ai()` | GET / POST `/v1/diagram/ai` | Describe a diagram in plain English via GET and get a rendered image back. Powered by AI. |
| `diagram_render()` | GET `/v1/diagram/render/{id}` | Render a previously saved diagram by ID. Public, no API key required. Supports ?format= and ?query= overrides. |
| `diagram_view()` | GET `/v1/diagram/view/{id}` | View a previously saved diagram as an HTML page. Public, no API key required. Iframe-embeddable with inline SVG rendering. |
| `jobs()` | GET `/v1/jobs/{id}` | Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: Completed… |
| `label()` | GET / POST `/v1/label` | Preview a thermal label via GET. Pass the same label object as a URL-encoded JSON string in query. Inside that JSON, text items use content… |
| `label_compile()` | POST `/v1/label/compile` | Compile a label to printer commands (tsc, zpl, epl, …). POST width, language, and elements. Text uses content and size (1-10), not text or… |
| `label_convert()` | POST `/v1/label/convert` | Convert printer commands from one language to another. POST source, from, and to. from is the source language (tsc, zpl, epl, …). to is the… |
| `label_parse()` | POST `/v1/label/parse` | Parse printer commands into structured elements. POST source and language (tsc, zpl, epl, …). |
| `label_render()` | GET `/v1/label/render/{id}` | Render a previously saved label by ID. Public, no API key required. Supports ?format= override. |
| `label_validate()` | POST `/v1/label/validate` | Validate printer commands. POST source (the raw commands) and language (tsc, zpl, epl, …). |
| `label_view()` | GET `/v1/label/view/{id}` | View a previously saved label as an HTML page. Public, no API key required. Iframe-embeddable with inline SVG rendering. |
| `qrcode()` | GET / POST `/v1/qrcode` | Generate a styled QR code via GET. Output: SVG (default) or PNG. Supports dot styles, gradients, custom corners and all QR versions. |
| `stats()` | GET `/v1/stats` | Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 mea… |
| `usage()` | GET `/v1/usage` | Return this account's Chartquery usage and credit balance. No body. Requires an API key. |

## License

MIT — see [LICENSE](LICENSE).
