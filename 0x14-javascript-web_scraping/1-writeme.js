#!/usr/bin/node

constant fs = require('fs');

try {
    fs.write(process.argv[2], process.argv[3]), 'utf-8', function (err, result) {
if (err) cosnole.log(err); });
} catch (err) {
  console.log(err);
}
