#!/usr/bin/env python
#coding:utf-8
"""
GIPHY APIを用いてGIF画像を検索しフェッチして画像データ（バイナリ）を標準出力に流すスクリプト
"""
import sys
import requests
import json
import random
import os
import signal

def kill_process(pid=os.getpid()):
    """
    プロセスツリーをkillする関数
    パイプラインとかで繋いでいるときにつかえる
    """
    os.killpg(pid, signal.SIGTERM)
    sys.exit(1)

def parse_args():
    """ 
     コマンドライン引数を解析
    """
    usage = "Usage: python {} WORD [-d, --downsample] | imgcat(or term-img)".format(__file__)
    
    if len(sys.argv) <= 1:
        sys.stderr.write(usage)
        kill_process()

    if len(sys.argv)==2 and sys.argv[1] in ["-d", "--downsample"]:
        sys.stderr.write(usage)
        kill_process()

    search_words = []
    downsamples = False
    for arg in sys.argv[1:]:
        if arg in ["-d", "--downsample"]:
            downsamples = True
        else:
            search_words.append(arg)

    return downsamples, search_words

if __name__=="__main__":
    
    # 引数から検索ワードを取得
    downsamples, search_words = parse_args()

    # 検索ワードが複数の場合はランダムに選択
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
    if downsamples:
        image_url = results["data"][rand_num]["images"]["fixed_height_downsampled"]["url"]
    else:
        image_url = results["data"][rand_num]["images"]["fixed_height"]["url"]

    # データをバイナリで標準出力に流す
    r = requests.get(image_url, stream='True')
    sys.stdout.buffer.write(r.raw.read()) 
    sys.stderr.write(image_url + "\n") 
