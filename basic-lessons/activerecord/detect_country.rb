require "rubygems"
require "active_record"
require "hirb"
require "hirb-unicode"
require "open-uri"
require "nokogiri"
require "kconv"

#------------------------------------------------------------
# Active Recordで実行して得られた結果をテーブル形式で表示する
#
# @param [String] active recordeでSQL操作を実行した結果
# @return [String] テーブル形式の出力
#------------------------------------------------------------
def pretty_print(str)
  puts Hirb::Helpers::AutoTable.render str
end

#------------------------------------------------------------
# スクレイピング用のフェッチ関数。urlにGETリクエストを送り、
# レスポンスをNokogiriでパースしてhtmlのdom treeとして返す
#
# @param [String] url
# @return [String] nokogiri dom tree
#------------------------------------------------------------
def fetch_page(url)
  charset = nil
  html = open(url) do |f|
    raise "Got 404 error" if f.status[0] == "404"
    charset = f.charset # 文字種別を取得
    f.read # htmlを読み込んで変数htmlに渡す
  end
  
  doc = Nokogiri::HTML.parse(html.toutf8, nil, 'utf-8') do |config|
    config.noblanks.strict.nonet
  end

  return doc
end

#------------------------------------------------------------
# htmlタグを除去する
#
# @param [String] htmlのテキスト
# @return [String] htmlのタグが除去されたテキスト
#------------------------------------------------------------
def remove_html_tags(text)
  return text.gsub(/<(".*?"|'.*?'|[^'"])*?>/, "")
end

# DB接続設定
ActiveRecord::Base.establish_connection(
  adapter:  "mysql2",
  host:     "localhost",
  username: "root",
  password: "edgepj123",
  database: "wifi",
)
# テーブルにアクセスするためのクラスを宣言
class City < ActiveRecord::Base
  self.table_name = 'cities'
  belongs_to :country, class_name: "Country", foreign_key: "country_id"
end
class Country < ActiveRecord::Base
  self.table_name = 'countries'
  has_many :cities, class_name: "City", dependent: :destroy
end

# 引数から記事URLを取得してフェッチ
if ARGV.length != 1
  STDERR.puts "invalid argument"
  exit
end
permalink = ARGV[0]
html = fetch_page(permalink)

# 記事タイトルと内容を取得
post_title   = html.css(".entry-title > abbr").inner_text.strip
post_content = remove_html_tags(html.css(".entry-content > p").collect{|p| p.inner_text}.join(""))

if post_title.nil? || post_content.nil?
  STDERR.puts "post_title or post_content got nil"
  exit
end

# タイトルと内容から国名を判断
all_countries_regex = Country.pluck(:name).join("|")
all_cities_regex    = City.pluck(:name).join("|")
# pretty_print Country.cities
#   Country.all.each do |c|
# end
regex = "(#{all_countries_regex})" #|#{all_cities_regex})"
match_countries = post_title.match(/#{regex}/)
p match_countries
