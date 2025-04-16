
let son = document.querySelector(".jsp");
let son1 = document.querySelector(".jsp1");
let son3 = document.querySelector(".jsp2");


let start = 1000;
let end = 6453;

let duration = 100; 
let stepTime = Math.floor(duration / end);


let counter = setInterval(function () {
  start++;
  son.textContent = "+" + start;

  if (start == end) {
    clearInterval(counter); 
  }
}, stepTime );

let start1 = 0;
let end1 = 245;

let duration1 = 5000; 
let stepTime1 = Math.floor(duration1 / end1);


let counter1 = setInterval(function () {
  start1++;
  son1.textContent = "+" +  start1;

  if (start1 == end1) {
    clearInterval(counter1); 
  }
}, stepTime1);

let start3 = 0;
let end3 = 5; 

let duration3 = 5000; 
let stepTime3 = Math.floor(duration3 / end3);


let counter3 = setInterval(function () {
  start3++;
  son3.textContent = "+" +  start3+ "  " + "yil";

  if (start3 == end3) {
    clearInterval(counter3); 
  }
}, stepTime3);