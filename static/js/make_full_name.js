

// Функция для обновления поля "Full Name"
function updateFullName() {
    var lastName = document.getElementById('lastName').value || '';
    var firstName = document.getElementById('firstName').value || '';
    var middleName = document.getElementById('middleName').value || '';

    var fullName = lastName + " " + firstName + " " + middleName;
    document.getElementById("full_name").value = fullName.trim();
}
