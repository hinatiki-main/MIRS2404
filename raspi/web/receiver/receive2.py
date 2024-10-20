import requests
import time
import hashlib

API_URL = 'http://mirs2404-command.okakabase.net/api/button_states'

# データのハッシュ値を計算する関数
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# データ取得関数
def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()  # HTTPエラーをチェック
    return response.json()

def main():
    # 初期データの取得とハッシュ計算
    old_data = fetch_data()
    old_hash = calculate_hash(str(old_data))

    while True:
        try:
            # データの再取得
            new_data = fetch_data()
            new_hash = calculate_hash(str(new_data))

            # ハッシュを比較して変更があった場合にメッセージを出力
            if new_hash != old_hash:
                button1_pressed = new_data.get('button1')
                button2_pressed = new_data.get('button2')
                button3_pressed = new_data.get('button3')

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

                old_hash = new_hash

        except requests.exceptions.RequestException as e:
            print(f'HTTPリクエストエラー: {e}')
        except Exception as e:
            print(f'エラーが発生しました: {e}')

        # 0.5秒待機
        time.sleep(0.01)

if __name__ == "__main__":
    main()
