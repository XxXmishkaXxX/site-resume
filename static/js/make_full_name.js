function createNameFields() {
    var nameFieldsDiv = document.getElementById("nameFields");
    var fields = ["Last Name", "First Name", "Middle Name"];

    fields.forEach(function (field) {
        var inputDiv = document.createElement("div");
        var label = document.createElement("p");
        label.textContent = field + ":";
        inputDiv.appendChild(label);

        var input = document.createElement("input");
        input.setAttribute("type", "text");
        input.setAttribute("name", field.toLowerCase().replace(" ", "_"));
        input.setAttribute("maxlength", "100");
        input.addEventListener("input", updateFullName);

        inputDiv.appendChild(input);
        nameFieldsDiv.appendChild(inputDiv);
    });
}

// Функция для обновления поля "Full Name"
function updateFullName() {
    var lastName = document.querySelector('input[name="last_name"]').value || '';
    var firstName = document.querySelector('input[name="first_name"]').value || '';
    var middleName = document.querySelector('input[name="middle_name"]').value || '';

    var fullName = lastName + " " + firstName + " " + middleName;
    document.getElementById("full_name").value = fullName.trim();
}

// Вызываем функцию создания полей при загрузке страницы
window.onload = createNameFields;
