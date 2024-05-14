function deletePost(postId) {
                const csrfToken = document.getElementById('deleteForm').querySelector('input[name="csrfmiddlewaretoken"]').value;

                // Отправка AJAX-запроса на удаление поста
                $.ajax({
                    url: `/wall/api/posts/${postId}/delete/`,
                    type: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    },
                    success: function (data) {
                        const postElement = document.getElementById(`post-${postId}`);
                        if (postElement) {
                            postElement.remove();
                        }
                    },
                    error: function (xhr, status, error) {
                        // Обработка ошибок
                        console.error(error);
                    }
                });
            }