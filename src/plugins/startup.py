import aiocqhttp
import nonebot
from loguru import logger
from nonebot import on_startup, on_websocket_connect
from websocket_client import client

@on_startup
async def startup():
    logger.debug('start init...')
    await client.connect()



@on_websocket_connect
async def connect(event: aiocqhttp.Event):
    bot = nonebot.get_bot()
    groups = await bot.get_group_list()
    logger.info(f'Connected to {len(groups)} groups')
    await bot.send_private_msg(user_id=2180302542, message="机器人已启动")
    logger.success('Connected')
