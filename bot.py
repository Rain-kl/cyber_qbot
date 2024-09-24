from os import path
import nonebot
from loguru import logger

import config

logger.add("logs/runtime.log", rotation="1 day", retention="7 days", level="DEBUG")

# 在主线程中启动和监听
if __name__ == "__main__":
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'src', 'plugins'),
        'src.plugins'
    )
    nonebot.run()
