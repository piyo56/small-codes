#!/usr/bin/env python
#coding:utf-8
import sys
import requests
import json
import random

# コマンドライン引数から検索ワードを取得（複数の場合はそこからランダムに選ぶ）
if not (len(sys.argv) > 1):
    sys.stderr.write("usage: python fetch_image.py [search words]\n")
    with open("./error.png", "rb") as f:
        sys.stdout.buffer.write(f.read())
    sys.exit(1)

search_words = sys.argv[1:]
rand_num = random.randint(0, len(search_words)-1)
search_word = search_words[rand_num]

# GIPHYでgifを検索してその中から1つ選んでurlを取得する
api_key = "dc6zaTOxFJmzC"
query = search_word.replace(" ", "+")

web_site = "http://api.giphy.com/v1/gifs/search"
GET_args = "?api_key={}&q={}".format(api_key, query)

request_url = web_site + GET_args

r = requests.get(request_url, stream='True')
results = json.loads(r.text)
hit_image_nums = len(results["data"])
rand_num = random.randint(0, hit_image_nums-1)
#image_url = results["data"][rand_num]["images"]["fixed_height_downsampled"]["url"]
image_url = results["data"][rand_num]["images"]["fixed_height"]["url"]

# gif画像を取得してバイナリを標準出力に流す
sys.stderr.write(image_url + "\n")

r = requests.get(image_url, stream='True')
sys.stdout.buffer.write(r.raw.read()) 
