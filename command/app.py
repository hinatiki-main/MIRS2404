from flask import Flask, render_template, request, jsonify
import websockets, asyncio

asyncio = Flask(__name__)

# グローバル変数でボタンの状態を保持
button_states = {
    'button1': False,
    'button2': False,
    'button3': False
}

async def send_to_raspberry(message):
    url = "ws://localhost:5011"
    async with websockets.connect(url) as websocket:
        await websocket.send(message)

# ボタンの状態を受け取るエンドポイント
@asyncio.route('/api/button_state', methods=['POST'])
async def receive_button_state():
    global button_states
    data = request.get_json()
    button = data.get('button')
    pressed = data.get('pressed')
    await send_to_raspberry(button)
    if button in button_states and isinstance(pressed, bool):
        button_states[button] = pressed
        return jsonify({'message': '状態を受け取りました'}), 200
    else:
        return jsonify({'message': '無効なデータです'}), 400

@asyncio.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


if __name__ == '__main__':
    asyncio.run(host='0.0.0.0', port=5010)