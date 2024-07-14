'use strict';

function restore() {
  score1El.textContent = 0;
  score2El.textContent = 0;
  diceEl.classList.add('hidden');
}

function updatePlayerCurr() {
  if (current_player) curr1El.textContent = current_scroll;
  else curr2El.textContent = current_scroll;
}

function rollDice() {
  const dice = Math.trunc(Math.random() * 6 + 1);
  diceEl.classList.remove('hidden');
  diceEl.src = `dice-${dice}.png`;
  if (dice === 1) {
    switchPlayers();
  } else {
    current_scroll += dice;
    updatePlayerCurr();
  }
}

function switchPlayers() {
  if (current_player) {
    player1Panel.classList.remove('player--active');
    player2Panel.classList.add('player--active');
    curr1El.textContent = 0;
  } else {
    player2Panel.classList.remove('player--active');
    player1Panel.classList.add('player--active');
    curr2El.textContent = 0;
  }
  current_player = !current_player;
  current_scroll = 0;
}

function hold() {
  if (current_player)
    score1El.textContent = +score1El.textContent + current_scroll;
  else score2El.textContent = +score2El.textContent + current_scroll;
  switchPlayers();
}

let current_player = true;
let current_scroll = 0;

const score1El = document.getElementById('score--0');
const score2El = document.getElementById('score--1');
const curr1El = document.getElementById('current--0');
const curr2El = document.getElementById('current--1');
const diceEl = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');
const player1Panel = document.querySelector('.player--0');
const player2Panel = document.querySelector('.player--1');

restore();

btnNew.addEventListener('click', restore);
btnRoll.addEventListener('click', rollDice);
btnHold.addEventListener('click', hold);
