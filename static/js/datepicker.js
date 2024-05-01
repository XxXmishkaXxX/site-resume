$(document).ready(function () {
        $('#birth_date').datepicker({
            uiLibrary: 'bootstrap5',
            locale: 'ru-ru',
            format: '%d/%m/%Y',
            maxDate: new Date()
        });
    })