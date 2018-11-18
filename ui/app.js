"use strict";

function getUrl(endpoint) {
  return `${window.location.origin}/api/${endpoint}`;
}

function addFormListener() {
  document.getElementById("form").addEventListener("submit", e => {
    const measureList = document.getElementById("measure-list");
    const measure = measureList[measureList.selectedIndex].value;

    const userList = document.getElementById("user-list");
    const user = userList[userList.selectedIndex].value;

    loadWeightedScores(measure, user);
  });
}

function loadWeightedScores(measure, user) {
  const url = getUrl("weighted-scores");
  const result = document.getElementById("result");

  /* Remove all children except for the header */
  while (result.children.length > 1) {
    result.removeChild(result.children[1]);
  }

  fetch(`${url}/${measure}/${user}`)
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

function loadList(endpoint) {
  const url = getUrl(endpoint);
  const list = document.getElementById(endpoint);

  fetch(url)
    .then(res => {
      return res.json();
    })
    .then(json => {
      for (const elem of json) {
        const option = document.createElement("option");

        const text = document.createTextNode(elem);
        option.appendChild(text);

        list.appendChild(option);
      }
    })
    .catch(err => {
      console.log(err);
    });
}

function main() {
  addFormListener();
  loadList("measure-list");
  loadList("user-list");
}

window.onload = main;
