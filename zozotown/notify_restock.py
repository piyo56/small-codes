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

# ページソースを取得してBeautifulSoupのオブジェクトを返す
def fetch_page(url):
    time.sleep(1)
    target_page = requests.get(url)
    enc = target_page.encoding
    if target_page.status_code == 200:
        soup = BeautifulSoup(target_page.text.encode(enc), "lxml")
        return soup
    else:
        print_error("failed to fetch page source (status code:{})".format(target_page.status_code))
        return None

if __name__ == "__main__":
    target_url = "http://zozo.jp/shop/journalstandard/goods/12677141/?rid=1019"
    soup = fetch_page(target_url)

    if soup is not None:
        cart_div = soup.select(".cart")
        
        # 今回のアイテムの場合、カラー3色のサイズ3種で合計9つのdivがヒット
        if not cart_div[0].text.strip() == "完売しました":
            Notifier.notify("再入荷しました！！", title="ZOZO", open=target_url, sound='Ping')
