const button = document.getElementById('showNextDiv');
const divs = ['div1', 'div2', 'div3', 'div4'];
let currentIndex = 0;

button.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % divs.length;
  divs.forEach((id, index) => {
    const divElement = document.getElementById(id);
    const isCurrentDiv = index === currentIndex;
    divElement.classList[isCurrentDiv ? 'remove' : 'add']('d-none');

    // Проверяем, является ли текущий блок последним
    if (isCurrentDiv && index === divs.length - 1) {
      console.log(button)
      button.classList.add('d-none'); // Скрываем кнопку "Далее"
    } else {
      button.classList.remove('d-none'); // Показываем кнопку "Далее" для всех остальных случаев
    }
  });
});