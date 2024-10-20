from flask import Flask, render_template, request, jsonify
import socket_connection as sc
import os

app = Flask(__name__)

# グローバル変数でボタンの状態を保持
button_states = {
    'button1': False,
    'button2': False,
    'button3': False
}

# ボタンの状態を受け取るエンドポイント
@app.route('/api/button_state', methods=['POST'])
async def receive_button_state():
    global button_states
    data = request.get_json()
    button = data.get('button')
    pressed = data.get('pressed')

    await sc.send_to_raspberry(button)  # websocket通信

    if button in button_states and isinstance(pressed, bool):
        button_states[button] = pressed
        return jsonify({'message': '状態を受け取りました'}), 200
    else:
        return jsonify({'message': '無効なデータです'}), 400

@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=5010, 
        debug=True, 
        extra_files=[
            os.path.join(os.getcwd(), 'static'),
            os.path.join(os.getcwd(), 'templates')
        ]
    )
