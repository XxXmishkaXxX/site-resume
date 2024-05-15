$(document).ready(function () {
    $('#create_profile').submit(function (event) {
        event.preventDefault();

        // Получаем данные формы
        var formData = $(this).serialize();

        // Отправляем данные на сервер
        $.ajax({
            type: "POST",
            url: $(this).attr('action'), // URL для отправки данных формы
            data: formData,
            success: function (response) {
                // Если ответ успешный, перенаправляем пользователя
                window.location.href = response.redirect_url;
            },
            error: function (xhr, textStatus, errorThrown) {
                var errorData = xhr.responseJSON;

                showErrors(errorData);
            }
        });
    });

    function showErrors(errorData) {
        var errorHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">';

        for (var key in errorData) {
                if (errorData.hasOwnProperty(key)) {
                    if (key === 'full_name') {
                        errorHTML += "Ошибка с вводом ФИО";
                        errorHTML += '<br>';
                    }
                    if (key === 'birth_date'){
                        errorHTML += "Ошибка с датой";
                        errorHTML += '<br>';
                    }
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
    }
});
