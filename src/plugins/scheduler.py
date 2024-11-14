import asyncio

import nonebot
from loguru import logger

from websocket_client import client


@nonebot.scheduler.scheduled_job('interval', seconds=2)
async def _():
    try:
        await client.send_tmq()
        response_model = await asyncio.wait_for(client.receive_message(), timeout=1.5)
        if response_model:
            logger.debug(f"Send -> Private: {response_model}")
            bot=nonebot.get_bot()
            await bot.send_private_msg(user_id=response_model.user_id, message=response_model.msg)

    except asyncio.TimeoutError:
        pass
        # print("Task took too long, skipped.")

