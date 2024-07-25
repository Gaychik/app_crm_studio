$(document).ready(function(){
    // Применение маски к полю ввода
    $('#login-phone').mask('+7 (000) 000-00-00', {
        clearIfNotMatch: true
        }
    );

    $('#register-phone').mask('+7 (000) 000-00-00', {
        clearIfNotMatch: true
        }
    );
    // Сохранение значения placeholder атрибута
    $('#login-phone').attr('placeholder', '+7 (___) ___-__-__');
    $('#register-phone').attr('placeholder', '+7 (___) ___-__-__');
});