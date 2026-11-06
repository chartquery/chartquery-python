"""Use the asyncio client."""

import asyncio

from chartquery import AsyncChartQueryClient


async def main() -> None:
    async with AsyncChartQueryClient() as client:  # reads CHARTQUERY_API_KEY
        response = await client.chart_ai(
            prompt="Monthly revenue 2026 as a bar chart: Jan 10, Feb 14, Mar 18"
        )
        print(response.data)


asyncio.run(main())
