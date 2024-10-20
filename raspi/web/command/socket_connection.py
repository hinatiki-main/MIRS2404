import websockets

async def send_to_raspberry(message):
    url = "ws://localhost:5011"
    async with websockets.connect(url) as websocket:
        await websocket.send(message)