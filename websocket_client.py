import json
import websockets
from loguru import logger


class WebSocketClient:
    def __init__(self):
        self.uri = None
        self.websocket = None
        self.temp_mq = []

    async def connect(self, uri: str):
        self.uri = uri
        self.websocket = await websockets.connect(self.uri)
        logger.success("Connected!")

    async def send_message(self, message: dict):
        if self.websocket:
            try:
                await self.websocket.send(json.dumps(message))
            except websockets.exceptions.ConnectionClosedError:
                self.temp_mq.append(message)

    async def send_tmq(self):
        if self.temp_mq:
            await self.send_message(self.temp_mq[0])
            self.temp_mq.pop(0)

    async def receive_message(self):
        if self.websocket:
            try:
                response = await self.websocket.recv()
                return json.loads(response)
            except websockets.exceptions.ConnectionClosedError:
                logger.critical("Cyber Engine Connection Lost!")
                await self.connect(self.uri)

        else:
            return None

    async def close(self):
        if self.websocket:
            await self.websocket.close()
            logger.success("Connection closed!")


client = WebSocketClient()
