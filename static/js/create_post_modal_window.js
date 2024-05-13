var modalCreatePost = document.getElementById('modalCreatePost');
var openModalFormCreatePostBtn = document.getElementById('openModalFormCreatePostBtn');
var closeBtn = document.getElementsByClassName('close')[1];

openModalFormCreatePostBtn.onclick = function() {
    modalCreatePost.style.display = 'block';
}

closeBtn.onclick = function() {
    modalCreatePost.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target === modalCreatePost) {
        modalCreatePost.style.display = 'none';
    }
}