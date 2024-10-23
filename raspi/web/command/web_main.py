from flask import Flask, render_template, request, jsonify, json
import socket_connection as sc
import configparser

app = Flask(__name__)

#configの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('../config.ini', encoding='utf-8')

# グローバル変数でボタンの状態を保持
button_states = {
    'button1': False,
    'button2': False,
    'button3': False
}

@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")

# ボタンの状態を受け取るエンドポイント
@app.route('/api/button_state', methods=['POST'])
async def receive_button_state():
    global button_states
    data = request.get_json()
    
    button = data.get('button')
    pressed = data.get('pressed')

    await sc.send_to_raspberry(data)#websocket通信

    if button in button_states and isinstance(pressed, bool):
        button_states[button] = pressed
        return jsonify({'message': '状態を受け取りました'}), 200
    else:
        return jsonify({'message': '無効なデータです'}), 400

if __name__ == '__main__':
    HOST = config_ini.get('web_main', 'HOST')
    PORT = config_ini.get('web_main', 'PORT')

    app.run(host=HOST, port=PORT)
    #デバッグ用コマンド↓
    #flask --app web_main run --host 192.168.1.12 --port 5010 --debug --extra-files templates/*:static/*