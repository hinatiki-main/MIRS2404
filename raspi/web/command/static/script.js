var origin_URL = window.location.href;

// ボタンの表示切替
//TODO ボタンの切り替え処理
function display_switching(buttonId, state) {
    const button1 = document.getElementById('button1');
    const button2 = document.getElementById('button2');

    if (buttonId == "button1" && state == false) {
        button1.style.display = 'none';
        button2.style.display = 'inline-block';
        button4.style.display = 'inline-block';
    } else if (buttonId == "button4" && state == false) {
        button2.style.display = 'none';
        button4.style.display = 'none';
        button1.style.display = 'inline-block';
    }
}

//POSTとボタン
function sendButtonState(buttonId, button_state, run_state) {
    fetch(origin_URL + '/api/button_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'button': buttonId, 'pressed': button_state , 'start': run_state})
    })
    .catch(error => {
        console.error('通信エラー:', error);
    });
}

function setupButton(buttonId) {
    const button = document.getElementById(buttonId);
    let isPressed = false;
    let stopModal = null;  // モーダルのインスタンスをグローバルに保持

    // モーダルの初期化
    if (buttonId === 'button1') {
        stopModal = new bootstrap.Modal(document.getElementById('stopModal'));
        
        // OKボタンのクリックイベントを一度だけ設定
        document.getElementById('okButton').addEventListener('click', function() {
            display_switching('button1', false);
            sendButtonState('button1', false, false);
            isPressed = false;
            button.classList.remove('pressed');
        });

        // モーダルの外部をクリックした場合もOKボタンを押したときと同じ動作をするように設定
        document.getElementById('stopModal').addEventListener('hidden.bs.modal', function() {
            display_switching('button1', false);
            sendButtonState('button1', false, false);
            isPressed = false;
            button.classList.remove('pressed');
        });
    }

    function startSendingState() {
        if (!isPressed) {
            isPressed = true;
            button.classList.add('pressed');
            sendButtonState(buttonId, true, false);
        
            if (buttonId === 'button1') {  // 停止ボタンの場合
                stopModal.show();  // 保存したモーダルインスタンスを使用
            }
        
            display_switching(buttonId, true);
        }
    }

    function stopSendingState() {
        if (isPressed && buttonId !== 'button1') {  // 停止ボタン以外の場合
            isPressed = false;
            button.classList.remove('pressed');
            display_switching(buttonId, false);

            if (buttonId == 'button4') { //水出し終了(button4)で走行開始
                sendButtonState(null, null, true);
            } else {
                sendButtonState(buttonId, false, false);
            }
        }
    }

    // タッチイベント
    button.addEventListener('touchstart', function(e) {
        e.preventDefault();
        startSendingState();
    }, false);

    button.addEventListener('touchend', function(e) {
        e.preventDefault();
        stopSendingState();
    }, false);

    // マウスイベント（デバッグ用）
    button.addEventListener('mousedown', function(e) {
        e.preventDefault();
        startSendingState();
    }, false);

    button.addEventListener('mouseup', function(e) {
        e.preventDefault();
        stopSendingState();
    }, false);

    button.addEventListener('mouseleave', function(e) {
        e.preventDefault();
        stopSendingState();
    }, false);
}

window.addEventListener('load', function() {
    setupButton('button1');
    setupButton('button2');
    setupButton('button4');
});