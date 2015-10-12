
/*
Solution for codeeval challenge #99 (CALCULATE DISTANCE)
https://www.codeeval.com/open_challenges/99/

AUTHOR: Erik Johnson
DATE: 2015-OCT-04

DISCUSSION:
*/

var fs = require('fs'), 
    argv = process.argv,
    filename = argv[2],
    lines = fs.readFileSync(filename, 'utf-8').split('\n');

// process each line
lines.forEach(function (line) {

    var dx, dy, l, p1 = [], p2 = [];
        
    if (line.trim().length == 0) {
        return; // continue (except this isn't a control loop)
    }

    l = line.split(') (');
    l[0].substring(1).split(',').forEach(function (s) {
        p1.push(Number(s));
    });

    l[1].substring(0, l[1].length - 1).split(',').forEach(function (s) {
        p2.push(Number(s));
    });

    dx = Math.abs(p1[0] - p2[0]);
    dy = Math.abs(p1[1] - p2[1]);
    console.log(Math.sqrt(dx * dx + dy * dy));
});

