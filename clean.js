// Clean SAST fixture: safe text sink, no HTML assignment.

function renderGreeting(userInput) {
  const el = document.getElementById("greeting");
  el.textContent = userInput;
  return el;
}

module.exports = { renderGreeting };
