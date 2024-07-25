document.addEventListener('DOMContentLoaded', () => {
    const flashes = document.querySelectorAll('.flashes li');
    if (flashes) {
        setTimeout(() => {
            flashes.forEach(flash => {
                flash.style.display = 'none';
            });
        }, 5000); // 5 секунд
    }
});


