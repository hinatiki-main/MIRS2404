import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input("サーバーに送りたいメッセージを入力してな: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"サーバーからの返事: {response}")

if __name__ == "__main__":
    asyncio.run(hello())
