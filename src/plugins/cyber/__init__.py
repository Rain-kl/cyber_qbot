from loguru import logger
from nonebot import on_natural_language, NLPSession, IntentCommand, on_command, CommandSession
from websocket_client import client
from model import InputModel


@on_command('send')
async def send(session: CommandSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    if session.event.detail_type == 'group':
        return
    else:
        logger.debug(f"Received <- Private({session.event.user_id}): {session.event.message}")
        input_model = InputModel(
            user_id=session.event.user_id,
            msg=str(session.event.message)
        )
        await client.send_message(input_model.model_dump())


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language()
async def _(session: NLPSession):
    return IntentCommand(100.0, 'send')
