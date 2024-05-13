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

// Проверяем ширину экрана и выполняем код только на экранах шириной менее 768 пикселей
if (window.innerWidth < 932) {
    // Добавляем обработчик события изменения размеров окна для адаптации меню
    window.addEventListener('resize', () => {
        // Если экран стал шире 768 пикселей, скрываем меню
        if (window.innerWidth >= 430) {
            navMenu.style.display = 'none';
        }
    });

    // Добавляем проверку, хватает ли места для отображения меню справа
    const checkMenuPosition = () => {
        const menuWidth = navMenu.getBoundingClientRect().width;
        const screenWidth = window.innerWidth;
        const menuLeft = navMenu.getBoundingClientRect().left;
        // Если меню выходит за правый край экрана, сдвигаем его влево
        if (menuLeft + menuWidth > screenWidth) {
            navMenu.style.left = `-${menuWidth - (screenWidth - menuLeft)}px`;
        } else {
            navMenu.style.left = '';
        }
    };

    // Вызываем проверку при открытии меню
    menuButton.addEventListener('click', checkMenuPosition);

    // Вызываем проверку при изменении размеров окна
    window.addEventListener('resize', checkMenuPosition);
}
