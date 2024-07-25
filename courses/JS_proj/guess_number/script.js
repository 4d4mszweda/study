'use strict';

let correct_number = 0;
const message = document.querySelector('.message');
const score = document.querySelector('.score');
const num = document.querySelector('.number');
const high_score = document.querySelector('.highscore');

function resotre() {
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
  correct_number = Math.trunc(Math.random() * 20 + 1);
  score.textContent = 20;
  message.textContent = 'Start guessing...';
  num.textContent = '?';
  document.querySelector('.guess').value = '';
}

function infoMess(msg) {
  score.textContent = score.textContent - 1;
  if (+score.textContent > 0) {
    message.textContent = msg;
  } else {
    message.textContent = 'YOU ARE LOSER';
  }
}

resotre();

const again_btn = document
  .querySelector('.again')
  .addEventListener('click', resotre);

const check_btn = document
  .querySelector('.check')
  .addEventListener('click', function () {
    const guess = +document.querySelector('.guess').value;

    if (!guess || guess > 20 || guess <= 0) {
      message.textContent = 'WRONG NUMBER !!';
    } else if (guess === correct_number) {
      message.textContent = 'YOU ARE RIGHT';
      num.textContent = correct_number;
      document.querySelector('body').style.backgroundColor = '#60b347';
      document.querySelector('.number').style.width = '30rem';
      if (+high_score.textContent < +score.textContent) {
        high_score.textContent = score.textContent;
      }
    } else if (correct_number > guess) {
      infoMess('too Low');
    } else if (correct_number < guess) {
      infoMess('too High');
    }
  });
