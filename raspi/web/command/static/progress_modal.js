// progress_modal.js

export function showProgressModal() {
    const progressModalElement = document.getElementById('progressModal');
    const progressModal = new bootstrap.Modal(progressModalElement);

    const progressContainer = document.querySelector('.progress'); // プログレスバー全体
    const progressBar = document.getElementById('progressBar'); // 青いバー
    const waterMessage = document.getElementById('waterMessage'); // 「水をどうぞ」のメッセージ

    progressBar.style.width = '0%';
    progressContainer.style.opacity = '1'; // プログレスバーの初期表示
    waterMessage.style.opacity = '0'; // メッセージを非表示にする
    waterMessage.style.display = 'none'; // 最初は完全に非表示

    // モーダル全体をフェードイン
    progressModalElement.style.opacity = '0'; // 初期状態を透明に
    progressModal.show(); // モーダルを表示するが透明
    setTimeout(() => {
        progressModalElement.style.transition = 'opacity 0.5s ease';
        progressModalElement.style.opacity = '1'; // フェードイン
    }, 10); // 微小な遅延を設定してフェードイン開始

    let progress = 0;

    // プログレスバーの進捗
    const interval = setInterval(() => {
        progress += 0.25;
        progressBar.style.width = `${progress}%`;

        if (progress >= 100) {
            clearInterval(interval);

            // プログレスバー全体をフェードアウト
            progressContainer.style.transition = 'opacity 0.5s ease';
            progressContainer.style.opacity = '0'; // フェードアウト
            setTimeout(() => {
                progressContainer.style.display = 'none'; // 完全に消す

                // 「水をどうぞ」のメッセージをフェードイン
                waterMessage.style.display = 'block';
                waterMessage.style.transition = 'opacity 0.5s ease';
                waterMessage.style.opacity = '1'; // フェードイン
                setTimeout(() => {
                    // 3秒後にモーダル全体をフェードアウト
                    progressModalElement.style.transition = 'opacity 0.5s ease';
                    progressModalElement.style.opacity = '0'; // フェードアウト
                    setTimeout(() => {
                        progressModal.hide(); // モーダルを閉じる

                        // モーダルが閉じた後にリセット処理を実行
                        setTimeout(() => {
                            // 次回用にリセット
                            progressContainer.style.display = ''; // プログレスバーを元に戻す
                            progressContainer.style.opacity = '1';
                            progressBar.style.width = '0%'; // ここでリセット
                            waterMessage.style.display = 'none';
                            waterMessage.style.opacity = '0';
                            progressModalElement.style.opacity = '1';
                        }, 500); // モーダル完全非表示後にリセット
                    }, 500); // モーダル全体のフェードアウト時間
                }, 3000); // 3秒後にフェードアウト開始
            }, 500); // プログレスバー全体のフェードアウト時間
        }
    }, 20); // 20ミリ秒間隔で進捗
}
