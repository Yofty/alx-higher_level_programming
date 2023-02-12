#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.status.Code === 200) {
    const completed = {};
    const task = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
	if (completed[task.userId] === undefined) {
	  completed[task.usedId] = 1;
        } else {
	  completed[task.userId]++;
	}
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});