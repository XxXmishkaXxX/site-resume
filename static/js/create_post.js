function createPost() {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const postContent = document.getElementById('postContent').value;
    const postImages = document.getElementById('postImages').files;

    const formData = new FormData();
    formData.append('content', postContent);
    formData.append('csrfmiddlewaretoken', csrfToken);
    for (let i = 0; i < postImages.length; i++) {
        formData.append('images', postImages[i]);
    }

    // Отправка AJAX-запроса на создание поста
    $.ajax({
        url: '/wall/api/posts/create/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            location.reload();
        },

        error: function(xhr, status, error) {
            // Обработка ошибок
            console.error(error);
        }
    });

}

