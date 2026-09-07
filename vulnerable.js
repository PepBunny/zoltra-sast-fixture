// Deliberately vulnerable SAST fixture (do not copy into product code).

function renderGreeting(userInput) {
  const el = document.getElementById("greeting");
  el.innerHTML = userInput;
  return el;
}

module.exports = { renderGreeting };
