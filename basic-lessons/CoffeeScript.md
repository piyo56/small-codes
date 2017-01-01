基本
--

* コメント

```
# comment -> なし
###{comment}### -> /*{comment}*/
```

* var不要
* セミコロン不要
* （）省略可能
* 変数展開Rubyと同じ#{}
* ヒアドキュメントPythonと同じ"""

配列
--

```
# ちょくちょくRubyやPythonがまじっている

m = [0..5] #=>[0, 1, 2, 3, 4, 5] 
m = [0...5] #=>[0, 1, 2, 3, 4] 

m[1..3] #=> m.slice(1,4) =  [1,2,3]
m[..3] #=> m.slice(0,4) =  [0,1,2,3]
m[1..]
m[..]
m[-1]

if 5 in [1, 3, 5] => true

# 同じように文字列も取り出せる
```


オブジェクト
--

```
# m = {name: "taguchi", score: 80}

m = name: "taguchi", score: 80

# コンマがないのがキモい
m = 
  name: "taguchi"
  score: 80

n = 
  name: "taguchi"
  score:
    first: 80
    second: 70
    thied: 90

obj =
  score: 52

if "score" of obj  => true
```

if
---

```
if score > 60 then alert score else alert "hoge!"

alert score if score > 60 # 後置

msg = if score > 60 then "OK" else "NG" # 三項演算
```

比較演算子
--

```
# is ===
# isnt !==

# alert "ok" if 10 < x < 20

# [true] yes on,  [false] no off

# and or not
```

switch
--

```
# [js]
switch (signal) {
  case "red":
    alert("STOP");
    break;
  case "blue":
  case "green":
    alert("GO");
    break;
  case "yellow":
    alert("CAUTION");
    break;
  default:
    alert("wrong signal")
}

[coffee]
switch signal
  when "red"
    alert "STOP"
  when "blue", "green" then alert "GO"
  when "yellow" then alert "CAUTION"
  else alert "wrong signal"
}
```


