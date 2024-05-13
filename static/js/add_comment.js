


    function addComment(postId) {

        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const commentText = document.getElementById('commentText_' + postId).value;

        const formData = new FormData();
        formData.append('text', commentText);
        formData.append('post_id',postId)
        formData.append('csrfmiddlewaretoken', csrfToken)

        $.ajax({
            url: '/wall/api/comment/create/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                console.log(data)
                const commentList = document.getElementById('comments_list_' + postId);
                const newCommentHTML = `
                    <div class="comment">
                        <div class="avatar">
                            <img src="${data.user_profile.avatar}" alt="avatar-commenter" style="max-width: 50px">
                        </div>
                        <div class="full_name">
                            <p>${data.user_profile.full_name}</p>
                        </div>
                        <div class="comment_text">${data.comment.text}</div>
                        <div class="date-create-comment">${data.comment.created_at}</div>
                    </div>
                `;
                commentList.insertAdjacentHTML('beforeend', newCommentHTML);
                document.getElementById('addComment_' + postId).reset();
            },
            error: function(xhr, status, error) {
                // Обработка ошибок
                console.error(error);
            }
        });
    }
