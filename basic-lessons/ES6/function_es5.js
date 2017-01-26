// ES5
'use strict';

function loop(func, count) {
  var count = count || 3;
  for (var i = 0; i < count; i++) {
    func();
  }
}

function sum() {
  var result = 0;
  for (var i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  return result;
}

loop(function(){ console.log('hello')}); // hello hello hello
console.log(sum(1, 2, 3, 4)); // 10
