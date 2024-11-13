// progress_modal.js

export function showProgressModal() {
    const progressModal = new bootstrap.Modal(document.getElementById('progressModal'));
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
            progressModal.hide();
        }
    }, 20);
}
