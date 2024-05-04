$(document).ready(function () {
        $('#birth_date').datepicker({
            uiLibrary: 'bootstrap5',
            locale: 'ru-ru',
            format: 'mm/dd/yyyy',
            maxDate: new Date()
        });
    })