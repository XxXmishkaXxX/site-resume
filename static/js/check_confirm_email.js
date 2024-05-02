$(document).ready(function (o, v) {
    $('#signup_form').submit(function (event) {
        event.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            success: function (data) {
                var email = data.form.fields.email.value;

                showAlert('Вам на почту '+ email +' пришло письмо с ссылкой, перейдите по ссылке для ' +
                    'подтверждения почты', 'alert-primary');

                checkEmailConfirmation();
            },
            error: function (xhr) {
                var errorData = JSON.parse(xhr.responseText);

                var errorMessage = JSON.parse(errorData.html)
                showAllauthError(errorMessage);
            }
        });
    });


    function checkEmailConfirmation() {
        $.ajax({
            url: '/accounts/check-email-confirmation/',
            type: 'GET',
            success: function (data) {

                if (data.confirmed) {

                    showAlert('Почта успешно подтверждена, сейчас вас перенаправит на создание профиля',
                        'alert-success');

                    setTimeout(function () {
                        window.location.href = '/profile/create/';
                    }, 5000);
                } else {

                    setTimeout(checkEmailConfirmation, 5000);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                var errorMessage = JSON.parse(errorThrown.responseText);
                showAllauthError(errorMessage);
            }
        });
    }


    function showAlert(message, alertType) {
        var alertHTML = '<div class="alert ' + alertType + ' alert-dismissible fade show" role="alert">' +
            message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
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

    function showAllauthError(errorData) {
    var errorHTML = '<div class="alert alert-danger alert-dismissible fade show" role="alert">';


    for (var key in errorData) {

        if (errorData.hasOwnProperty(key)) {
            errorHTML += errorData[key][0].message;
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
}

});
