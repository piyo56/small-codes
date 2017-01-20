#coding: utf-8
import sys
import time
from bs4 import BeautifulSoup
import requests
from pync import Notifier

"""
    zozotownでどうしてもほしいアイテムの再入荷を通知するスクリプト
    最近は再入荷ボタンが出現しない傾向にあるので困っている
"""

def fetch_page(url):
    """
    ページソースを取得してBeautifulSoupのオブジェクトを返す
    """
    time.sleep(1)
    target_page = requests.get(url)
    enc = target_page.encoding
    if target_page.status_code == 200:
        soup = BeautifulSoup(target_page.text.encode(enc), "lxml")
        return soup
    else:
        print("failed to fetch page source (status code:{})".format(target_page.status_code))
        return None

if __name__ == "__main__":
    target_url = "http://zozo.jp/shop/abahouse/goods-sale/14802339/?did=32762540&rid=1095"
    soup = fetch_page(target_url)

    if soup is not None:
        cart_div = soup.select(".cart")
        
        # 今回のアイテムの場合、カラー3色のサイズ3種で合計9つのdivがヒット
        if not cart_div[5].text.strip() == "完売しました":
            Notifier.notify("再入荷しました！！", title="ZOZO", open=target_url, sound='Ping')
