
document.getElementById('flip-register').addEventListener('click', function() { 
    document.querySelector('.container').classList.add('flip'); 
}); 
 
document.getElementById('flip-login').addEventListener('click', function() { 
    document.querySelector('.container').classList.remove('flip'); 
});


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