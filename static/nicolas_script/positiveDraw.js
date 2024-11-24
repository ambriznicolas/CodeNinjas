function createCanvas() {
  var side = 100;
  var tbody = document.getElementById("tablebody");

  for (var i = 0; i < side; ++i) {
    var row = document.createElement("tr");

    for (var j = 0; j < side; ++j) {
      var cell = document.createElement("td");
      row.appendChild(cell);
    }

    tbody.appendChild(row);
  }

  document
    .getElementById("canvas")
    .addEventListener("mousemove", processMouseMove, false);
}

function processMouseMove(e) {
  if (e.target.tagName.toLowerCase() == "td") {
    if (e.ctrlKey) {
      e.target.setAttribute("class", "purple");
    }

    if (e.shiftKey) {
      e.target.setAttribute("class", "blue");
    }
  }
}

window.addEventListener("load", createCanvas, false);
