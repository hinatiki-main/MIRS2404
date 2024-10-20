import asyncio
import websockets
import json

WS_URLS = [
    'wss://mirs2404-command.okakabase.net',
    'wss://mirs2404-command.okakabase.net'
]

async def monitor_websocket(ws_url):
    async with websockets.connect(ws_url) as websocket:
        print(f"監視を開始します... {ws_url}")
        while True:
            try:
                # サーバーからメッセージを受信
                message = await websocket.recv()
                data = json.loads(message)

                button1_pressed = data.get('button1')
                button2_pressed = data.get('button2')
                button3_pressed = data.get('button3')

                if button1_pressed:
                    print(f'{ws_url} - ボタン1が押されています')
                    # ボタン1が押されているときの処理をここに追加

                if button2_pressed:
                    print(f'{ws_url} - ボタン2が押されています')
                    # ボタン2が押されているときの処理をここに追加

                if button3_pressed:
                    print(f'{ws_url} - ボタン3が押されています')
                    # ボタン3が押されているときの処理をここに追加

                if not any([button1_pressed, button2_pressed, button3_pressed]):
                    print(f'{ws_url} - どのボタンも押されていません')

            except websockets.exceptions.ConnectionClosed as e:
                print(f'WebSocket接続エラー: {e} - {ws_url}')
                break
            except Exception as e:
                print(f'エラーが発生しました: {e} - {ws_url}')

async def main():
    # すべてのWebSocket URLに対して接続タスクを作成
    tasks = [monitor_websocket(url) for url in WS_URLS]
    # 並行して実行
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

