# デバッグ
```php
var_dump($var); // 型と中身を出力できる
```
# 文字列

ダブルクオーテーションで囲った場合は特殊文字や変数を展開する
シングルクオーテーションで囲った場合は展開しない

```php
//変数展開を行う場合いずれも可
$name = "hoge";

echo "My name is $hoge";
echo "My name is ${hoge}";
echo "My name is {$hoge}";

```

# 配列

PHPの配列の基本は連想配列、keyを省略することで通常の配列
最後のコンマはつけたまま可能
php 5.4以降では大カッコ($colors=["red", "blue", "green"])が使用可能

```php
$sales = array(
  "taguchi"    => 800,
  "fkoji"      => 800,
  "dotinstall" => 800,
);
```

配列を回すときは foreach

```php
$colors=["red", "blue", "green"];

foreach($colos as $key => $value){
  echo "($key) $value";
}

// foreachの引数は省略可能
foreach($colos as $value){
  echo "$value";
}

```

foreach for if whileではコロン構文と呼ばれる表記も可能
HTMLなどに埋め込むときに可読性を高めることが出来る

```php
foreach ($colors as $color) :
  echo $color;
endforeach;

// 埋め込み時
<ul>
  <?php foreach ($colors as $color) : ?>
  <li><?php echo $color; ?></li>
  <?php endforeach; ?>
</ul>
```

# 関数

デフォルト値が使用可能

```php
function sayHi($name = "piyo56"){
  echo "Hi, $name";
}

// 使いそうな組み込み関数
strlen("cat"); #文字数を返す
mb_strlen("ねこ"); #マルチバイト用
printf("%d円", 123); #cのprintfに近い
count(array());  #配列の要素を返す
implode("separator", array());   # joinに同じ
```

# クラス

```php
class User{
  //property
  public $name;

  //constructor
  public function __construct($name){
    $this->name = $name;
  }

  //method
  public function sayHi(){
    echo "hi, i am $this->name!";
  }
}

$tom = new User("Tom");
$bob = new User("Bob");

echo $tom->name;
$bob->sayHi();
```

# 例外処理

```php
function div($a, $b){
  try {
    if($b === 0){
      throw new Exception("cannot divided by 0 !")
    }
    echo $a / $b;
  } catch(Exception $e) {
    echo $e->getMessage();
  }
}

div(7, 2);
div(7, 0);
```

# フォーム処理

```html
<?php
$username = "";
if ($_SERVER['REQUEST_METHOD'] === "POST"){
  $username = $_POST["username"];
  $err = false;
  if(strlen($username) > 8){
    $err = true;
  }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Check username</title>
</head>
<body>
  <form action="" method="POST">
    <input type="text" name="username" placeholder="username" value="<?php echo htmlspecialchars($username, ENT_QUOTES, "UTF-8")?>">
    <input type="submit" value="Check!">
    <?php if ($err) { echo "Too long!";} ?>
  </form>
</body>
</html>
```

# Cookie

```php

// set
setcookie("username", "taguchi");
setcookie("username", "taguchi", time()+60*60); # 1時間後に消える

// get
echo $_COOKIE["username"];

// delete
setcookie("username", "taguchi", time()-60*60);

```

# Session

```php
// start
session_start();

// set
$_SESSION["username"] = "taguchi";

// get
echo $_SESSION["username"];

// delete
unset($_SESSION["username"]);
```

