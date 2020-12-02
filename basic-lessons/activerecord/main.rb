require 'active_record'
require 'logger'
require 'hirb'
require 'hirb-unicode'

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

ActiveRecord::Base.establish_connection(
  "adapter" => "sqlite3",
  "database" => "./blog.db"
)

ActiveRecord::Base.logger = Logger.new(STDOUT)

class Post < ActiveRecord::Base
  scope :top3, -> {
    order("created_at").limit(3)
  }
  validates :title, :presence => true
  validates :body,  :length => {:minimum => 5}

  has_many :comments
end

class Comment < ActiveRecord::Base
  belongs_to :post
end

# # 05
# pretty_print Post.all
# pretty_print Post.first
# pretty_print Post.last
# pretty_print Post.find(3)

# # 06
# pretty_print Post.where(:title => "title1")
# pretty_print Post.where("title = ? and id = ?", "title1", 1)
# pretty_print Post.where("id > ?", 2)

# # 07
# pretty_print Post.where(:id => 1..3)
# pretty_print Post.where(:id => [1, 3])
# pretty_print Post.order("id desc").first(3)
# pretty_print Post.order("id desc").limit(3)
# pretty_print Post.top3

# 08
# pretty_print Post.where(:title => "title3").first_or_create
# pretty_print Post.where(:title => "title5").first_or_create
# pretty_print Post.where(:title => "title6").first_or_create do |p|
#   p.body = "hello6"
# end

# # 09
# post = Post.find(1)
# post.title = "(new)title1"
# post.save

# post.update_attribute(:title, "(new2)title1")
# post.update_attributes(:title => "nnn", :body => "hhh")
# Post.where(:id => 1..2).update_all(:title => "nnn3", :body => "hhh3")
#pretty_print Post.first

# # 10
# # delete:  record fast
# # desttoy: object slow
# Post.find(1).delete
# Post.where(:id => 1..2).delete_all

# # 11
# post = Post.new(:body => "123")
# #post.save!
#
# if !post.save
#   p post.errors.messages
# end

post = Post.find(1)
post.comments.each do |comment|
  pretty_print comment.body
end
