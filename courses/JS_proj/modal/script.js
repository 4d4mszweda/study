'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btns = document.querySelectorAll('.show-modal');
const close_btn = document.querySelector('.close-modal');

for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener('click', function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
  });
}

const close_fn = () => {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

close_btn.addEventListener('click', close_fn);

overlay.addEventListener('click', close_fn);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') {
    close_fn();
  }
});
