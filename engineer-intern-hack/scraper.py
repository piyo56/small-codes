import sys
import time
from bs4 import BeautifulSoup
import requests
import re
import gmplot
import googlemaps

# 地域
regions = ["東京都", "千葉県"]

# エラーを表示する
def print_error(title, url, address=""):
    #print("-"*3 + " error " + "-"*40)
    print("\ttitle: {}".format(title))
    print("\turl: {}".format(url))
    if len(address):
        print("\taddress: {}".format(address))
    print()
    #print("-"*50)

# ページソースを取得してBeautifulSoupのオブジェクトを返す
def fetch_page_source(url):
    time.sleep(1)
    target_page = requests.get(url)
    if target_page.status_code == 200:
        soup = BeautifulSoup(target_page.text, "lxml")
        return soup
    else:
        print_error("failed to fetch page source (status code:{})".format(target_page.status_code))
        return None

# 住所部分を抜き出す関数
def extract_adrresses(target_url):
    soup = fetch_page_source(target_url)
    if soup is not None:
        enterprise_infos = []
        title_name = "".join(soup.find("title").contents[0])
        target_div = soup.select("#internList > li")

        # 正規表現
        div_pattern = re.compile(r"勤務先の住所")
        address_pattern = re.compile(r"(((" + r"|".join(regions) + r").*?[0-9０-９-丁目]+).*?)[<>]")
        
        # 検索ページの各企業エントリに対して
        for div in target_div:
            # タイトルとURLを取得
            title = div.select(".interntitle")[0].contents[0]
            url  = div.select(".interntitle")[0].get("href")

            print("\t\t*{}".format(title))

            # URL先に行って住所を取得
            time.sleep(1)
            c_soup = fetch_page_source(url)
            info_divs = str(c_soup.select(".internInfo")[1])

            address_div = re.search(div_pattern, info_divs)
            if not address_div:
                print("\n-------> [error] failed to search address_div")
                print_error(title, url)
                continue

            address_part = info_divs[address_div.start():]
            address = re.search(address_pattern, address_part)
            if not address:
                #print("\n-------> [Warning] failed to search address str")
                #print("\n-------> [msg] This enterprise is outside of regions")
                #print_error(title, url)
                continue
            address = address.group(2)
            # print(address)
            # sys.stdin.read(1)
            enterprise_infos.append({\
                "title":   title,\
                "url":     url,\
                "address": address\
            })
        return enterprise_infos
    else:
        return []

def extract_next_search_page(current_page_url):
    soup = fetch_page_source(current_page_url)
    next_page_div = soup.select(".next")
    if next_page_div:
        return str(next_page_div[0].get("href"))
    else:
        return None

def parse():
    if len(sys.argv) < 2:
        print("usage: python /path/to/scraper.py [url of EngineerIntern search page]")
        sys.exit()
    else:
        return sys.argv[1]

if __name__ == "__main__":
    search_page = parse()

    print("start scraping...")
    enterprise_infos = []

    # スクレイピングで現在の検索ページとそれ以降のページの企業情報を全て取得
    while True:
        print("\t- {}".format(search_page))
        enterprise_infos.extend(extract_adrresses(search_page))

        search_page = extract_next_search_page(search_page)
        if search_page is None:
            break

    print("\n\t{} entries are found\n".format(len(enterprise_infos)))

    # GoogleMap初期化
    print("plotting Google Map...")
    geocoder = googlemaps.Client(key='AIzaSyAPO0FiAAXTs6me9JdLxhmZ4FL7kgC26ck')
    gmap = gmplot.GoogleMapPlotter(35.681233, 139.766944, 11) #東京駅を中心に

    # GoogleMapで位置を表示
    for enterprise in enterprise_infos:
        geocode_result = geocoder.geocode(enterprise["address"])
        if not geocode_result or len(geocode_result) == 0:
            print("-------> [error] failed to geocode")
            print_error(enterprise["title"], enterprise["url"], enterprise["address"])
            continue

        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        gmap.marker(lat, lng, 'red', title=enterprise["title"])

    print("writing out as my_map.html...")
    gmap.draw("my_map.html")
    print("\ndone")
