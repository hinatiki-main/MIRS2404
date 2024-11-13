// progress_modal.js

export function showProgressModal() {
    const progressModalElement = document.getElementById('progressModal');
    const progressModal = new bootstrap.Modal(progressModalElement);
    progressModal.show();

    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = '0%';

    let progress = 0;

    // 0.25%ずつ増加して20msごとに更新、8秒で100%に
    const interval = setInterval(() => {
        progress += 0.25;
        progressBar.style.width = `${progress}%`;

        if (progress >= 100) {
            clearInterval(interval);

            // 100%になったらフェードアウト開始
            progressModalElement.classList.add('fade-out');
            setTimeout(() => {
                progressModal.hide(); // フェードアウト後に非表示
                progressModalElement.classList.remove('fade-out'); // 次回表示のためにクラスを削除
            }, 500); // 500msのフェードアウト
        }
    }, 20);
}
