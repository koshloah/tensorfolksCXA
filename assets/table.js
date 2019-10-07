function startTimer () {
    console.log("start")
    setTimeout(stopTimer,2000);
}

function stopTimer () {
    console.log("end")
}

startTimer()

var table = document.getElementById("knn-table")
table.className = "table table-striped"

var table = document.getElementById("mba-table")
table.className = "table table-striped"

var table = document.getElementById("mba2-table")
table.className = "table table-striped"

console.log("fuck")
