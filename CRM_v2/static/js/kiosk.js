const ORDER_KEY = 'orders';

let selectedItems = [];

function saveItems() {
  localStorage.setItem(ORDER_KEY, JSON.stringify(selectedItems));
}

const selectButton = document.querySelectorAll('.select__button');
selectButton.forEach((button) => button.addEventListener('click', handleSelectedItem));

function handleSelectedItem(event) {
  event.preventDefault();
  const selectedItem = event.currentTarget.value;
  const newItem = {
    value: selectedItem,
    id: Date.now(),
  };
  selectedItems.push(newItem);
  printSelectedItem(newItem);
  saveItems();
}

function deleteItem(event) {
  const div = event.target.parentElement;
  div.remove();
  selectedItems = selectedItems.filter((item) => item.id !== parseInt(div.id));
  saveItems();
}

function printSelectedItem(newItem) {
  const selectedItemWrap = document.querySelector('.selected-items');
  const selectedDiv = document.createElement('div');
  selectedDiv.classList.add('selected-item');
  selectedDiv.id = newItem.id;

  const deleteButton = document.createElement('button');
  deleteButton.innerText = '❌';
  deleteButton.addEventListener('click', deleteItem);
  selectedDiv.appendChild(deleteButton);

  const itemNameSpan = document.createElement('span');
  const parsedItemValue = JSON.parse(newItem.value);
  itemNameSpan.innerText = parsedItemValue.Name;
  selectedDiv.appendChild(itemNameSpan);
  selectedItemWrap.appendChild(selectedDiv);
}

// TODO: url 파싱하지 않고 백에서 url을 보내줄 수는 없을까?
const currentURL = window.location.href;
const splitURL = currentURL.split('/');

const userUUID = splitURL[splitURL.length - 2];
const storeUUID = splitURL[splitURL.length - 1];

const endPointURL = `/new_order/${userUUID}/${storeUUID}`;

const paymentButton = document.querySelector('.payment__button');
paymentButton.addEventListener('click', () => {
  const localStorageData = JSON.parse(localStorage.getItem(ORDER_KEY));
  const itemInfo = localStorageData.map((item) => JSON.parse(item.value));

  fetch(endPointURL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(itemInfo),
  });

  localStorage.clear();

  const paymentModal = document.querySelector('.payment__modal');
  paymentModal.style.display = 'block';

  const countdown = document.querySelector('.countdown');
  let remainingTime = 5;
  countdown.innerText = remainingTime;

  const countdownInerval = setInterval(() => {
    remainingTime -= 1;
    countdown.innerText = remainingTime;

    if (remainingTime <= 0) {
      clearInterval(countdownInerval);
      window.location.href = '/';
    }
  }, 1000);
});
