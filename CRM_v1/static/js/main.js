// 아이디, 비밀번호 입력시 label 크기, 위치 변화
const loginInputs = document.querySelectorAll('.login__input');
const loginLabels = document.querySelectorAll('.login__label');

loginLabels.forEach((loginLabel, index) => {
  const loginInput = loginInputs[index];

  loginLabel.addEventListener('click', () => {
    loginInput.focus();
    loginLabel.classList.add('selected');
  });

  loginInput.addEventListener('focus', () => {
    loginLabel.classList.add('selected');
  });

  loginInput.addEventListener('focusout', () => {
    if (loginInput.value.length > 0) {
      loginLabel.classList.add('hidden');
    } else {
      loginLabel.classList.remove('hidden');
      loginLabel.classList.remove('selected');
    }
  });
});
