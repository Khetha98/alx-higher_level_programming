#!/usr/bin/node
const k = require('fs');

k.readFile(process.argv[2], (error, data) => {
  if (error) throw error;
  let content = data.toString();
  k.readFile(process.argv[3], (error, data) => {
    if (error) throw error;
    content += data.toString();
    k.writeFile(process.argv[4], content, (error) => {
      if (error) throw error;
    });
  });
});
