## ES6 （ES2015）

<img src="https://cdn-images-1.medium.com/max/800/1*raWO3dhM4jMjf9VY-kZzNg.png" alt="modern_js_pic" height="400">

### 概要

- ESはEcmaScriptの略でブラウザの仕様が含まれていない言語仕様
- 言わばJavaScriptはEcmaScriptのサブセット?実装?のようなもの
- すなわち自分の視点から言うと、ES◯◯はJavaScriptのバージョンのようなもの
- 一応毎年策定されている（ES2016, ES2017...）
- ES6から飛躍的に機能が増えた（class / generator / module などが含まれる最新仕様）

### 機能

- let constによる変数宣言

- クラス構文

  普段jsであまり複雑なことをやらないので今回初めてes5でのクラス構文を見たがよく意味がわからない。es6でやっとサポートされたとあってまぁ普通に書けるようになったという感じ。

- アロー関数による関数宣言

- 分割代入
	```javascript
	var name = Izmeal;
	var age  = 21;	
	```
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓

	```var [name, age] = ['Koyabu', 20];```

- 配列展開
	引数展開のようなもの
  ```
  var array = [1, 2, 3];
  console.log(...array);
  ```
	
- 関数のデフォルト引数
	```
	function multiply(a, b = 1) {
  		return a*b;
	}
	multiply(5); // 5
	```
- テンプレート文字列
	```
	var name = 'Koyabu'
	var hello = `My name is ${name}`
	console.log(hello)
	```

- Promise

  コールバック地獄さようなら


### 取り巻く技術(JSの闇っぽいところ)

[2016年にJavaScriptを学ぶとこんな感じ](https://medium.com/japan/2016%E5%B9%B4%E3%81%ABjavascript%E3%82%92%E5%AD%A6%E3%81%B6%E3%81%A8%E3%81%93%E3%82%93%E3%81%AA%E6%84%9F%E3%81%98-b969f5767d7c#.9zdg1w3rd)

#### トランスパイラ

- Babel、TypeScriptなど
- ES6は仕様が膨大でブラウザの実装が追いついていない。よってES6で書いてもそのままでは実行できないため、ES5またはES3などに変換してブラウザに実行させる。
- BabelはまさにES6を実行させるために使うといった感じで、TypeScriptはプラスアルファで静的型付けなどを導入出来るイメージ

#### モジュールシステム

- Browserify、Webpackなど
- ES6ではモジュールシステム(import/export)があるが、必要なファイルを事前に開発環境側で静的解析しガッチャンコして配布する仕組み


### 参考
- [ES2015 (ES6)についてのまとめ](http://qiita.com/tuno-tky/items/74ca595a9232bcbcd727)

- [春からはじめるモダンJavaScript / ES2015](http://qiita.com/mizchi/items/3bbb3f466a3b5011b509)

- [Modern JavaScript概観、そしてElectronへ](http://blog.satotaichi.info/modern-javascript_201701/) 

- [ES6時代のJavaScript](http://techlife.cookpad.com/entry/2015/02/02/094607) 

