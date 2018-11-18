"use strict";

function getUrl(endpoint) {
  return `${window.location.origin}/api/${endpoint}`;
}

function addFormListener() {
  document.getElementById("form").addEventListener("submit", e => {
    const userList = document.getElementById("user-list");
    const user = userList[userList.selectedIndex].value;
    console.log(`user: ${user}`);
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
