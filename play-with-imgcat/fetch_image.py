#!/usr/bin/env python
#coding:utf-8
import sys
import requests
import json
import random

# GIPHYでgifを検索してその中から1つ選んでurlを取得する
search_word = "Good Job"
api_key = "dc6zaTOxFJmzC"
query = search_word.replace(" ", "+")

web_site = "http://api.giphy.com/v1/gifs/search"
GET_args = "?api_key={}&q={}".format(api_key, query)

request_url = web_site + GET_args

r = requests.get(request_url, stream='True')
results = json.loads(r.text)
hit_image_nums = len(results["data"])
rand_num = random.randint(1, hit_image_nums)
image_url = results["data"][rand_num]["images"]["fixed_height_downsampled"]["url"]
#image_url = results["data"][rand_num]["images"]["fixed_height"]["url"]

# gif画像を取得してバイナリを標準出力に流す
sys.stderr.write(image_url + "\n")

r = requests.get(image_url, stream='True')
sys.stdout.buffer.write(r.raw.read()) 
