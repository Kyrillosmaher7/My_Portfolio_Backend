from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket
    ):
        await websocket.accept()

        self.connections.append(
            websocket
        )

    def disconnect(
        self,
        websocket: WebSocket
    ):
        self.connections.remove(
            websocket
        )

    async def broadcast(
        self,
        payload: dict
    ):
        dead_connections = []

        for ws in self.connections:

            try:
                await ws.send_json(
                    payload
                )

            except Exception:
                dead_connections.append(
                    ws
                )

        for ws in dead_connections:
            self.disconnect(ws)


manager = ConnectionManager()