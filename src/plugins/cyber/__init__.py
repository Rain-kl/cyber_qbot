from nonebot import on_natural_language, NLPSession, IntentCommand, on_command, CommandSession
from websocket_client import client


@on_command('send')
async def send(session: CommandSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    print(f"on_natural_language: {session.event.message}")
    print(f"on_natural_language: {session.event.user_id}")
    response = await client.send_message({
        'username': str(session.event.user_id),
        'msg': str(session.event.message)
    })
    print(response)
    await session.send(response)


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language()
async def _(session: NLPSession):
    return IntentCommand(100.0, 'send')
