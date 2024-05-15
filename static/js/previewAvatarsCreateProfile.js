
    function previewAvatar() {
        var preview1 = document.getElementById('avatarPreview1');
        var preview2 = document.getElementById('avatarPreview2');
        var preview3 = document.getElementById('avatarPreview3');
        var file = document.getElementById('avatar').files[0];
        var reader = new FileReader();

        reader.onloadend = function () {
            preview1.src = reader.result;
            preview2.src = reader.result;
            preview3.src = reader.result;
        }

        if (file) {
            reader.readAsDataURL(file);
        } else {
            preview1.src = "{% static 'image/default_avatar.jpg' %}";
            preview2.src = "{% static 'image/default_avatar.jpg' %}";
            preview3.src = "{% static 'image/default_avatar.jpg' %}";
        }
    }
