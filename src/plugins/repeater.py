from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


@on_command('repeat', aliases=('重复'))
async def repeat(session: CommandSession):
    print(session.current_arg)
    print(session.current_key)
    print(session.current_arg_filters)
    # 向用户发送天气预报
    await session.send("你刚刚说了：")