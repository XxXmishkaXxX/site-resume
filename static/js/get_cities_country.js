$(document).ready(function(){
    $('#country').change(function(){
        var country_name = $(this).val();
        $.ajax({
            url: "/api/get_cities_by_country/" + country_name + "/",
            type: "GET",
            success: function(data) {
                var citySelect = $('#city');
                citySelect.empty();

                $.each(data, function(index, city) {
                    citySelect.append($('<option>', {
                        value: city.id,
                        text: city.name
                    }));
                });

                $('#city_div').show();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // Отображение ошибки в консоли браузера
            }
        });
    });
});
