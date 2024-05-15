function likePost(postId) {
     const csrfToken = document.getElementById('like').querySelector('input[name="csrfmiddlewaretoken"]').value;
    // Отправляем запрос на сервер для создания лайка
    fetch('/wall/api/like/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':  csrfToken
        },
        body: JSON.stringify({post_id: postId})
    })
    .then(response => {
        if (response.ok) {
            return response.json().then(data => {
                const likesCountElement = document.getElementById(`likes-count-${postId}`);
                if (likesCountElement && data.detail === 'Лайк создан') {
                    const heartIcon = document.getElementById(`heart-svg-${postId}`);

                    heartIcon.classList.remove('bi-heart');
                    heartIcon.classList.add('bi-heart-fill');
                    likesCountElement.textContent = data.likes_count;
                }
                else{
                    const heartIcon = document.getElementById(`heart-svg-${postId}`);

                    heartIcon.classList.remove('bi-heart-fill');
                    heartIcon.classList.add('bi-heart');
                    likesCountElement.textContent = data.likes_count;
                }
            });
        } else {
            // Если возникла другая ошибка, выводим сообщение об ошибке
            return response.json().then(data => {
                console.error(data.detail);
            });
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}

