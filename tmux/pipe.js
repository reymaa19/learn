var readline = require("readline");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});

rl.on("line", function (line) {
    console.log(
        "LINE: ",
        line.split(" ").reduce((sum, x) => sum + +x, 0),
    );
});

# echo "5 7 9\n 11 13 15" | node pipe.js
