import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"受け取ったメッセージ: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 5011):
        print("サーバーが起動したで、ポート5011で待っとるで！")
        await asyncio.Future()  # 無限に待つ

if __name__ == "__main__":
    asyncio.run(main())
