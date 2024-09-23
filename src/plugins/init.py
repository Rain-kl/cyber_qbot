import asyncio
from loguru import logger
import nonebot
import aiocqhttp

from nonebot import on_startup, get_bot, on_websocket_connect


@on_startup
async def startup():
    logger.debug('start init...')


@on_websocket_connect
async def connect(event: aiocqhttp.Event):
    bot = nonebot.get_bot()
    groups = await bot.get_group_list()
    logger.info(f'Connected to {len(groups)} groups')
    await bot.send_private_msg(user_id=2180302542, message="机器人已启动")
    logger.success('Connected')
