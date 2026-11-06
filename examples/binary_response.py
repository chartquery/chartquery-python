"""Save a binary response to a file."""

import os

from chartquery import BinaryResponse, ChartQueryClient

with ChartQueryClient(os.environ["CHARTQUERY_API_KEY"]) as client:
    response = client.qrcode(data="https://chartquery.com", format="png")
    if isinstance(response, BinaryResponse):
        with open("qrcode.png", "wb") as file:
            file.write(response.bytes)
        print(f"Saved qrcode.png ({response.content_type}, {len(response.bytes)} bytes)")
    else:
        print(response.data)
