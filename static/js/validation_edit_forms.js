$(document).ready(function() {

    // Функция для отображения уведомления об ошибках
    function showErrors(errorData) {
        var errorHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">';
        for (var key in errorData) {
            if (errorData.hasOwnProperty(key)) {
                if (key === 'full_name') {
                    errorHTML += "Ошибка с вводом ФИО";
                } else if (key === 'birth_date') {
                    errorHTML += "Ошибка с датой";
                } else if (key === "oldpassword"){
                    errorHTML += "Ваш пароль не совпадает с введенным"
                }
                else {
                    errorHTML += errorData[key];
                }
                errorHTML += '<br>';
            }
        }

        errorHTML += '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
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
        errorHTML = ''
    }

    // Обработчик отправки формы профиля
    $('form[name="profileForm"]').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Создаем объект FormData для сбора данных формы
        var formData = new FormData(this);
        console.log("!!!")
        console.log(formData.values())
        // Отправляем данные формы на сервер с помощью AJAX
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function(data) {
                location.reload();
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log(xhr.data)
                var errorData = xhr.responseJSON;
                showErrors(errorData);
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

    // Обработчик отправки формы смены пароля
    $('form[name="changePasswordForm"]').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Создаем объект FormData для сбора данных формы
         var formData = new FormData(this);
        formData.append('form_name', 'changePasswordForm');
        // Отправляем данные формы на сервер с помощью AJAX
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function(data) {
                location.reload();
            },
            error: function(xhr, textStatus, errorThrown) {
                var errorData = xhr.responseJSON;
                showErrors(errorData);
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
});
