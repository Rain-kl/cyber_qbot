import asyncio

import nonebot

from websocket_client import client


@nonebot.scheduler.scheduled_job('interval', seconds=2)
async def _():
    try:
        data = await asyncio.wait_for(client.receive_message(), timeout=1.5)
        if data:
            print(data)
    except asyncio.TimeoutError:
        pass
        # print("Task took too long, skipped.")
