// Function to scroll the terminal to the bottom
function scrollToBottom() {
  const terminalBody = document.getElementById('terminal-body');
  terminalBody.scrollTop = terminalBody.scrollHeight;
}

// Focus input field when clicking the terminal
const terminalBody = document.getElementById('terminal-body');
terminalBody.addEventListener('click', () => {
  document.getElementById('command-input').focus();
});

// Handle command input
const commandInput = document.getElementById('command-input');
const commandOutput = document.getElementById('command-output');

commandInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
      const command = commandInput.value.trim();

      commandOutput.innerHTML += `<div><span class="user">Tawfiq@portfolio</span>:<span class="path">~</span>$ ${command}</div>`;
      scrollToBottom();

  }
});

// Clear input and scroll after server response
document.body.addEventListener('htmx:afterRequest', () => {
  commandInput.value = '';
  scrollToBottom();
});

// Function to reload the page with an effect
function reloadPage() {
  document.getElementById('terminal').classList.add('reload-effect');
  // Uncomment to enable delayed reload:
  // setTimeout(() => location.reload(), 3000);
}

// Initialize canvas
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Setup matrix effect with English and Arabic letters
const englishLetters = 'ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/';
const arabicLetters = 'أبتثجحخدذرزسشصضطظعغفقكلمنهوي٠١٢٣٤٥٦٧٨٩!@#$%^&*()_+-=[]{}|;:,.<>?/';
let selectedLetters = englishLetters.repeat(4) + arabicLetters.repeat(4);
let fontSize = Math.max(10, Math.floor(window.innerWidth / 150));
let columns = Math.floor(canvas.width / fontSize);
let drops = Array(columns).fill(1);

// Function to set language
function setLanguage(lang) {
  selectedLetters = lang === 'arabic' ? arabicLetters.repeat(6) : englishLetters.repeat(6);
  localStorage.setItem('selectedLanguage', lang);
}

// Load language preference on page load
window.onload = () => {
  const savedLang = localStorage.getItem('selectedLanguage') || 'english';
  setLanguage(savedLang);
};

// Handle window resize
window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  fontSize = Math.max(10, Math.floor(window.innerWidth / 150));
  columns = Math.floor(canvas.width / fontSize);
  drops = Array(columns).fill(1);
});

// Draw matrix effect
function draw() {
  ctx.fillStyle = 'rgba(0, 0, 0, 0.3)'; // Slightly darker background for better contrast
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  
  drops.forEach((drop, i) => {
      const text = selectedLetters[Math.floor(Math.random() * selectedLetters.length)];
      ctx.fillStyle = '#0f0';
      ctx.fillText(text, i * fontSize, drop * fontSize);
      drops[i] = drop * fontSize > canvas.height && Math.random() > 0.95 ? 0 : drop + 1;
  });
}

// Start animation loop
setInterval(draw, 33);
