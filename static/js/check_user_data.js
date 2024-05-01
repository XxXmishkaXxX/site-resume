$(document).ready(function () {
    $('#login_form').submit(function (event) {
        event.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            success: function () {
                   checkEmailConfirmation()
             },
            error: function (xhr) {
                var errorData = JSON.parse(xhr.responseText);

                var errorMessage = JSON.parse(errorData.html)
                showErrors(errorMessage);
            }
        });
    });

    function showAlert(message, alertType) {
        var alertHTML = '<div class="alert ' + alertType + ' alert-dismissible fade show" role="alert">' +
            message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
        $('#alerts').append(alertHTML);
    }

    function showErrors(errorData) {
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

    function checkEmailConfirmation() {
        $.ajax({
            url: '/accounts/check-email-confirmation/',
            type: 'GET',
            success: function (data) {
                if (data.confirmed) {
                    window.location.href = '/feed/'
                } else {
                    showAlert('Ваша почта не подтверждена. Пожалуйста, подтвердите свой адрес электронной почты.',
                        'alert-warning');
                }
            }
        })
    }
})

