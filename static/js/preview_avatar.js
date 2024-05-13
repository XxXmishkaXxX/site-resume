function previewAvatar() {
        console.log('Я сработал')
        const avatarInput = document.getElementById('avatar');
        const avatarPreview = document.getElementById('avatarPreview');
        const file = avatarInput.files[0];
        const reader = new FileReader();

        reader.onload = function(event) {
            avatarPreview.src = event.target.result;
            avatarPreview.style.display = 'block';
        };

        reader.readAsDataURL(file);
    }