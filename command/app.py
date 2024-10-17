from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# グローバル変数でボタンの状態を保持
button_states = {
    'button1': False,
    'button2': False,
    'button3': False
}

@app.route("/", methods=["GET","POST"])
def main_page():
    return render_template("index.html")

# ボタンの状態を受け取るエンドポイント
@app.route('/api/button_state', methods=['POST'])
def receive_button_state():
    global button_states
    data = request.get_json()
    button = data.get('button')
    pressed = data.get('pressed')
    if button in button_states and isinstance(pressed, bool):
        button_states[button] = pressed
        return jsonify({'message': '状態を受け取りました'}), 200
    else:
        return jsonify({'message': '無効なデータです'}), 400

# Raspberry Piにボタンの状態を送信するエンドポイント
@app.route('/api/button_states', methods=['GET'])
def send_button_states():
    global button_states
    return jsonify(button_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
