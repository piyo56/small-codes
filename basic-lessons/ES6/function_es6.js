// ES6
'use strict';

// デフォルト引数
function loop(func, count = 3) {
  for (var i = 0; i < count; i++) {
    func();
  }
}

// 可変長引数
function sum(...numbers) {
  return numbers.reduce(function(a, b) { return a + b; });
}

// アローでの関数表記
loop(() => {console.log('hello')}); // hello hello hello
console.log(sum(1, 2, 3, 4)); // 10
