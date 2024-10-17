import requests
import time

API_URL = 'https://mirs2404-command.okakabase.net/api/command'

while True:
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # HTTPエラーをチェック
        command = response.text.strip()

        if command == 'no_command':
            # 新しい命令がない場合は何もしない
            pass
        elif command in ['button1', 'button2', 'button3']:
            print(f'{command} が押されました')
        else:
            print('未知の命令です')

    except requests.exceptions.RequestException as e:
        print(f'HTTPリクエストエラー: {e}')
    except Exception as e:
        print(f'エラーが発生しました: {e}')

    time.sleep(1)  # 1秒ごとにサーバーをチェック
