#!/usr/bin/env python
#coding:utf-8
import sys
import requests
import json
import random

# コマンドライン引数を解析
def parse_args():
    if not (len(sys.argv) > 1):
        sys.stderr.write("usage: python fetch_image.py [search words]\n\n")
        sys.stderr.write("  -d, --downsample: use downsampled gif image\n\n")
        # imgcatにリダイレクトする流れなので
        # エラー用の透明画像を流しておく
        #with open("./error.png", "rb") as f:
        #    sys.stdout.buffer.write(f.read())
        sys.exit(1)
    
    search_words = []
    do_downsample = False
    for arg in sys.argv[1:]:
        if arg in ["-d", "--downsample"]:
            do_downsample = True
        else:
            search_words.append(arg)

    return do_downsample, search_words

if __name__=="__main__":
    
    # 引数から検索ワードを取得
    # 検索ワードが複数の場合はランダムに選択
    do_downsample, search_words = parse_args()
    rand_num = random.randint(0, len(search_words)-1)
    search_word = search_words[rand_num]

    # GIPHYでgifを検索してその中から1つを選ぶ
    api_key = "dc6zaTOxFJmzC"
    query = search_word.replace(" ", "+")

    web_site = "http://api.giphy.com/v1/gifs/search"
    GET_args = "?api_key={}&q={}".format(api_key, query)

    request_url = web_site + GET_args

    r = requests.get(request_url, stream='True')
    results = json.loads(r.text)
    hit_image_nums = len(results["data"])
    rand_num = random.randint(0, hit_image_nums-1)

    # URLからgif画像を取得
    if do_downsample:
        image_url = results["data"][rand_num]["images"]["fixed_height_downsampled"]["url"]
    else:
        image_url = results["data"][rand_num]["images"]["fixed_height"]["url"]

    # データをバイナリで標準出力に流す
    r = requests.get(image_url, stream='True')
    sys.stdout.buffer.write(r.raw.read()) 
    sys.stderr.write(image_url + "\n") 
