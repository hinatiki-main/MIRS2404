function sendButtonState(buttonId, state) {
    fetch('https://mirs2404-command.okakabase.net/api/button_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'button': buttonId, 'pressed': state })
    })
    .catch(error => {
        console.error('通信エラー:', error);
    });
}

function setupButton(buttonId) {
    const button = document.getElementById(buttonId);

    let isPressed = false;

    function startSendingState() {
        if (!isPressed) {
            isPressed = true;
            button.classList.add('pressed');
            sendButtonState(buttonId, true);
        }
    }

    function stopSendingState() {
        if (isPressed) {
            isPressed = false;
            button.classList.remove('pressed');
            sendButtonState(buttonId, false);
        }
    }

    // タッチイベント
    button.addEventListener('touchstart', function(e) {
        e.preventDefault(); // 既定の動作を無効化
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
    setupButton('button3');
});
