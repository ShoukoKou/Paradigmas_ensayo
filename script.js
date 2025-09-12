let timeLeft = 25 * 60; // 25 minutos en segundos
let timerId;
let isRunning = false;

const timerDisplay = document.getElementById('timer');
const startBtn = document.getElementById('start');
const pauseBtn = document.getElementById('pause');
const resetBtn = document.getElementById('reset');

function updateDisplay() {
  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  timerDisplay.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function startTimer() {
  if (!isRunning) {
    isRunning = true;
    timerId = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        updateDisplay();
      } else {
        clearInterval(timerId);
        isRunning = false;
        alert("¡Pomodoro completado! Tómate un descanso.");
      }
    }, 1000);
  }
}

function pauseTimer() {
  clearInterval(timerId);
  isRunning = false;
}

function resetTimer() {
  clearInterval(timerId);
  timeLeft = 25 * 60;
  isRunning = false;
  updateDisplay();
}

startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);

// Inicializar display
updateDisplay();