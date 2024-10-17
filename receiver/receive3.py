import asyncio
import websockets
import json

WS_URL = 'ws://mirs2404-command.okakabase.net/api/button_states'

async def main():
    async with websockets.connect(WS_URL) as websocket:
        print("監視を開始します...")
        while True:
            try:
                # サーバーからメッセージを受信
                message = await websocket.recv()
                data = json.loads(message)

                button1_pressed = data.get('button1')
                button2_pressed = data.get('button2')
                button3_pressed = data.get('button3')

                if button1_pressed:
                    print('ボタン1が押されています')
                    # ボタン1が押されているときの処理をここに追加

                if button2_pressed:
                    print('ボタン2が押されています')
                    # ボタン2が押されているときの処理をここに追加

                if button3_pressed:
                    print('ボタン3が押されています')
                    # ボタン3が押されているときの処理をここに追加

                if not any([button1_pressed, button2_pressed, button3_pressed]):
                    print('どのボタンも押されていません')

            except websockets.exceptions.ConnectionClosed as e:
                print(f'WebSocket接続エラー: {e}')
                break
            except Exception as e:
                print(f'エラーが発生しました: {e}')

if __name__ == "__main__":
    asyncio.run(main())
