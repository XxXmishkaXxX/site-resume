$(document).ready(function() {

    // Функция для отображения уведомления об ошибках
    function showErrors(errorData) {
        var errorHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">';
        for (var key in errorData) {
            if (errorData.hasOwnProperty(key)) {
                    errorHTML += errorData[key];
            }
        }

        errorHTML += '</div>';
        $('#alerts').append(errorHTML);
        setTimeout(function () {
            $('.alert').addClass('show');
        }, 100);
        setTimeout(function () {
            $('.alert').removeClass('show');
            setTimeout(function () {
                $('.alert').remove();
            }, 5000);
        }, 5000);
    }

    function showAlert(message, alertType) {
        var alertHTML = '<div class="alert ' + alertType + ' alert-dismissible fade show" role="alert">' +
            message + '</div>';
        $('#alerts').append(alertHTML);
        setTimeout(function () {
            $('.alert').addClass('show');
        }, 100);
        setTimeout(function () {
            $('.alert').removeClass('show');
            setTimeout(function () {
                $('.alert').remove();
            }, 500);
        }, 10000);
    }

    // Обработчик отправки формы профиля
    $('form[name="reset_password_form"]').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        var formData = new FormData(this);
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function(data) {
                var responseData = JSON.parse(data.html);

                if (responseData.success) {
                showAlert(responseData.success, 'alert-primary');
            } else {
                // Показываем пользователю сообщение об ошибке
                showErrors(responseData.error);
            }},

            error: function(xhr, textStatus, errorThrown) {
                showErrors('Произошла ошибка при отправке запроса.');
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
});
