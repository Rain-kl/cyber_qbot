import asyncio
from loguru import logger
import nonebot
from websocket_client import client
from model import ResponseModel

@nonebot.scheduler.scheduled_job('interval', seconds=2)
async def _():
    try:
        await client.send_tmq()
        data = await asyncio.wait_for(client.receive_message(), timeout=1.5)
        if data:
            response_model = ResponseModel(**data)
            logger.debug(f"Send -> Private: {data}")
            bot=nonebot.get_bot()
            await bot.send_private_msg(user_id=response_model.user_id, message=response_model.msg)

    except asyncio.TimeoutError:
        pass
        # print("Task took too long, skipped.")

