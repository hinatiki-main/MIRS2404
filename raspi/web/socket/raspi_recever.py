import asyncio
import websockets
import json
import configparser

#configの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('../config.ini', encoding='utf-8')

async def echo(websocket, path):
    async for server_data in websocket:
        data = json.loads(server_data)
        print(f"受け取ったメッセージ: {data}")

async def main():
    host = config_ini.get('raspi_recever', 'HOST')
    port = config_ini.get('raspi_recever', 'PORT')
    async with websockets.serve(echo, host, port):
        print(f"ポート{port}で待機")
        await asyncio.Future()  # 無限に待つ

if __name__ == "__main__":
    asyncio.run(main())
