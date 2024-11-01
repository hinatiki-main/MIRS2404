let countdownTimer;
let remainingTimeElement;
let remainingTime;
let setTime = 20;//タイマー

export function startCountdown() {

    // 既にカウントダウン中の場合はリセット
    if (countdownTimer) {
        clearInterval(countdownTimer);
        remainingTime = setTime; // 残り時間をリセット
        if (remainingTimeElement) {
            remainingTimeElement.textContent = ''; // 表示をリセット
        }
    }

    // 残り時間の表示エリアを取得、なければ新しく作成
    if (!remainingTimeElement) {
        remainingTimeElement = document.createElement('div');
        remainingTimeElement.className = 'fs-4 text-center mt-3';
        document.querySelector('.d-flex.flex-column.align-items-center').appendChild(remainingTimeElement);
    }

    // カウントダウン開始
    remainingTime = setTime;
    countdownTimer = setInterval(() => {
        remainingTime--;

        // 残り10秒のタイミングで表示
        if (remainingTime <= 10) {
            remainingTimeElement.textContent = `残り時間: ${remainingTime}秒`;
        }

        // カウントダウン終了処理
        if (remainingTime <= 0) {
            clearInterval(countdownTimer);
            remainingTimeElement.textContent = ''; // カウントダウン表示をリセット

            // button4要素を取得
            const button4 = document.getElementById('button4');
            
            // mousedownイベントを作成
            const mousedownEvent = new MouseEvent('mousedown', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            
            // mouseupイベントを作成
            const mouseupEvent = new MouseEvent('mouseup', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            
            // mousedownイベントを発火
            button4.dispatchEvent(mousedownEvent);
            
            // mouseupイベントを発火
            button4.dispatchEvent(mouseupEvent);
        }
    }, 1000);
}

export function stopCountdown() {
    if (countdownTimer) {
        clearInterval(countdownTimer);
        countdownTimer = null;
    }
    if (remainingTimeElement) {
        remainingTimeElement.textContent = ''; // 表示をリセット
    }
    remainingTime = setTime; // 残り時間をリセット
}