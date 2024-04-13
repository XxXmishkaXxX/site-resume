// Содержимое email_confirmation.js
$(document).ready(function() {
    // Функция для проверки статуса подтверждения почты
    function checkEmailConfirmation() {
        $.ajax({
            url: '/check-email-confirmation/', // Укажите URL вашего представления Django
            type: 'GET',
            success: function(data) {
                if (data.confirmed) {
                    // Если email подтвержден, перенаправляем на страницу создания профиля
                    window.location.href = '/create-profile/';
                } else {
                    // Если email не подтвержден, ждем некоторое время и повторяем проверку
                    setTimeout(checkEmailConfirmation, 5000); // Повторная проверка через 5 секунд
                }
            },
            error: function(error) {
                console.error('Ошибка при выполнении AJAX запроса:', error);
            }
        });
    }

    // Запускаем проверку статуса подтверждения почты при загрузке страницы
    checkEmailConfirmation();
});
