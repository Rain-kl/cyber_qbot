from pydantic import BaseModel


# 用户输入数据模型，用于传给ws服务端
class InputModel(BaseModel):
    role: str = "user"
    chanel: str = "qq"
    user_id: int  # 用户id
    msg: str  # 消息内容


# 服务端返回数据模型，用于传给用户
class ResponseModel(BaseModel):
    code: int = 200
    user_id: int  # 用户id
    msg: str  # 消息内容
    data: dict = {}
