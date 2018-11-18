"use strict";

function getUrl(endpoint) {
  return `${window.location.origin}/api/${endpoint}`;
}

function addFormListener() {
  document.getElementById("form").addEventListener("submit", e => {
    const userList = document.getElementById("user-list");
    const user = userList[userList.selectedIndex].value;

    loadWeightedScores(user);
  });
}

function loadWeightedScores(user) {
  const url = getUrl("weighted-scores");
  const result = document.getElementById("result");

  /* Remove all children except for the header */
  while (result.children.length > 1) {
    result.removeChild(result.children[1]);
  }

  fetch(`${url}/${user}`)
    .then(res => {
      return res.json();
    })
    .then(json => {
      for (const item of json) {
        const row = document.createElement("tr");

        const movie = document.createElement("td");
        const movieText = document.createTextNode(item.movie);
        movie.appendChild(movieText);

        const score = document.createElement("td");
        const scoreText = document.createTextNode(item.score.toFixed(4));
        score.appendChild(scoreText);

        row.appendChild(movie);
        row.appendChild(score);
        result.appendChild(row);
      }
    })
    .catch(err => {
      console.log(err);
    });
}

function loadUserList() {
  const url = getUrl("user-list");
  const userList = document.getElementById("user-list");

  fetch(url)
    .then(res => {
      return res.json();
    })
    .then(json => {
      for (const user of json) {
        const option = document.createElement("option");

        const text = document.createTextNode(user);
        option.appendChild(text);

        userList.appendChild(option);
      }
    })
    .catch(err => {
      console.log(err);
    });
}

function main() {
  addFormListener();
  loadUserList();
}

window.onload = main;
