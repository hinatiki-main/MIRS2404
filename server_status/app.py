import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

API_TOKEN = 'akgjUlc1fn1BvQ2VilraM3pe7uKGMb3aCG6yCWaN'
ACCOUNT_ID = 'ec259ffe8ab71de1ee9201cfd556c185'
TUNNEL_ID = 'e004c679-4459-4f40-ac6a-601407967ac3'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tunnel-status')
def tunnel_status():
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/cfd_tunnel/{TUNNEL_ID}'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        status = data.get('result', {}).get('status', 'unknown')
        return jsonify({'status': status})
    else:
        return jsonify({'error': response.status_code}), response.status_code

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
