var item1;
var item2;
var item3;
var item4;
var item5;

document.getElementById("changeList").onclick = newList;

function newList() {
    item1 = prompt("Enter first new thing");
    item2 = prompt("Enter second new thing");
    item3 = prompt("Enter third new thing");
    item4 = prompt("Enter fourth new thing");
    item5 = prompt("Enter fifth new thing");
    updateList();
}

function updateList() {
    document.getElementById("o").innerHTML = item1;
    document.getElementById("d").innerHTML = item2;
    document.getElementById("g").innerHTML = item3;
    document.getElementById("j").innerHTML = item4;
    document.getElementById("h").innerHTML = item5;
}