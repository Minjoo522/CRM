'use strict';

const loginInput = document.querySelector('.login__input');
const loginLabel = document.querySelector('.login__label');
loginInput.addEventListener('click', () => {
  loginLabel.classList.toggle('selected');
});
