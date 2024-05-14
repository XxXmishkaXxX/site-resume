const button = document.getElementById('showNextDiv');
const divs = ['div1', 'div2', 'div3', 'div4'];
let currentIndex = -1;

button.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % divs.length;
  divs.forEach((id, index) => {
    document.getElementById(id).classList[index === currentIndex ? 'remove' : 'add']('d-none');
  });
});
