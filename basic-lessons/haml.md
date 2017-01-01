Haml (HTML Abstraction Markup Language)
--

- [Official Site](http://haml.info/)
- written in Ruby

---

### 基本

- `!!!`はDOCTYPE宣言
- `%`でタグを表現
- インデントで階層構造を表現

### サンプルコード

```haml
!!!     
%html{:lang => "ja"}
  %head
    %meta(charset="UTF-8")
  %body
    hello world!

    / 一行でタグを閉じる
    %p hello

    / 要素に<を入れても一行になる
    / <>とすると親要素も
    %ul
      %li<>
        item
    
    / 同じdivタグ生成にも色々な記法あり
    %div{:id => "main", :class =>"myClass"}
    %div(id="main" class="myClass")
    %div#main.myClass 
      /emmetっぽい省略記法可能
    #main.myClass 
    

    / filter
    :css
      .myStatyle{
        color: red;
      }
    :javascript
      alert(1);
      if (1) {
        alert(2);
      }
    %div
      :escaped
        <html>
        </html>

    / Hamlの中でRubyの式を評価する

    %p total is #{5 * 3}
    %p= Time.now
    - x = 5
    %p= x
    
    / ループ
    - (1...10).each do |i|
      %p{:id => "item_#{i}"} #{i}

  / comment （htmlの<!--comment-->）
  /
    comment
    comment
    comment

  -# comment（Hamlファイル内のみのコメント）


```

```
# output with html5 format and double quotaion
haml -q -f index.haml index.html
```

