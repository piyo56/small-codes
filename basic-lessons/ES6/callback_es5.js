//ES5
"use strict";

function echo_a(callback) {
  console.log("a");
  setTimeout(callback, 1000);
}
function echo_b(callback) {
  console.log("b");
  setTimeout(callback, 1000);
}
function echo_c(callback) {
  console.log("c");
  setTimeout(callback, 1000);
}

//Promiseを使わない非同期を繋げる場合
echo_a(function(){
  echo_b(function(){
    echo_c(function(){});
  });
});
