import asyncio
import json
import websockets


class WebSocketClient:
    def __init__(self, uri: str):
        self.uri = uri
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect(self.uri)

    async def send_message(self, message: dict):
        if self.websocket:
            await self.websocket.send(json.dumps(message))
            print(f"Sent to server: {message}")

    async def receive_message(self):
        if self.websocket:
            response = await self.websocket.recv()
            print(f"Received from server: {response}")
            return json.loads(response)

        else:
            return None

    async def close(self):
        if self.websocket:
            await self.websocket.close()
            print("Connection closed")


client = WebSocketClient("ws://127.0.0.1:8600/ws/123")
