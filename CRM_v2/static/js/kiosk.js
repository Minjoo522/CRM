const selectedItems = document.querySelector('.selected-items');
const selectedItemDelete = document.querySelectorAll('.selected-item__delete');
const selectedItemMinus = document.querySelectorAll('.selected-item__minus');
const selectedItemPlus = document.querySelectorAll('.selectedt-item__plus');
const selectedItemQuantity = document.querySelectorAll('.selected-item__quantity');
const selectedItemAmount = document.querySelector('.selected-item__amount');
const payment = document.querySelector('.payment__button');

// 1. json으로 받아와서
// 2. 아이템 표시해준다
// 3. 쿠키에 저장한다(- id만 저장! 추가하면 쿠키에 추가추가추가, 삭제하면 삭제삭제삭제)
