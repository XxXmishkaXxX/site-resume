// Получаем ссылки на элементы DOM
const menuButton = document.querySelector('.menu button');
const navMenu = document.querySelector('.menu nav');

// Скрываем меню при загрузке страницы
navMenu.style.display = 'none';

// Добавляем обработчик события клика на кнопку бургер-меню
menuButton.addEventListener('click', () => {
    // Переключаем отображение меню
    if (navMenu.style.display === 'none') {
        navMenu.style.display = 'block';
    } else {
        navMenu.style.display = 'none';
    }
});

// Добавляем обработчик события клика на ссылки в меню для закрытия меню
navMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        // Скрываем меню после клика на ссылку
        navMenu.style.display = 'none';
    });
});