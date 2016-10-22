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
