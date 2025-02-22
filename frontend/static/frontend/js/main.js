// Function to scroll the terminal to the bottom
function scrollToBottom() {
  const terminalBody = document.getElementById('terminal-body');
  terminalBody.scrollTop = terminalBody.scrollHeight;
}

// Focus on the input field when clicking anywhere in the terminal
document.getElementById('terminal-body').addEventListener('click', function() {
  document.getElementById('command-input').focus();
});

document.getElementById('command-input').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    // Get the input value
    const command = this.value.trim();

    // Append the command to the #command-output div
    if (command) {
      const outputDiv = document.getElementById('command-output');
      outputDiv.innerHTML += `<div><span class="user">TawfiqSaid@portfolio</span>:<span class="path">~</span>$ ${command}</div>`;
      
      // Scroll to the bottom after appending new content
      scrollToBottom();
    }

  }
});

document.body.addEventListener('htmx:afterRequest', function(evt) {
  document.getElementById('command-input').value = '';
  
  // Scroll to the bottom after the server response is added
  scrollToBottom();
});

document.body.addEventListener('htmx:afterRequest', function(evt) {
  // Ensure the input field is cleared after the request
  document.getElementById('command-input').value = '';
});

