//ES6
"use strict";

function echo_a() { 
  console.log("a");
  return new Promise(function(resolve) {
    resolve();
  });
}

function echo_b() { 
  console.log("b");
  return new Promise( function(resolve) {
    resolve();
  });
}

function echo_c() { 
  console.log("c");
  return new Promise( function(resolve) {
    resolve();
  });
}

function sleep(time = 1000) {
  return new Promise(function(resolve) {
    var d1 = new Date().getTime();
    var d2 = new Date().getTime();
    while( d2 < d1+time ){
      d2 = new Date().getTime();
    }
    resolve();
  });
}

//Promiseを使って同期処理
echo_a()
.then(sleep)
.then(echo_b)
.then(sleep)
.then(echo_c);
