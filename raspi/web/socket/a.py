import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"受け取ったメッセージ: {message}")

async def main():
    port = 5011
    async with websockets.serve(echo, "localhost", port):
        print(f"ポート{port}で待機")
        await asyncio.Future()  # 無限に待つ

if __name__ == "__main__":
    asyncio.run(main())
