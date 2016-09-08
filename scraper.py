import sys
import time
from bs4 import BeautifulSoup
import requests
import re
import gmplot
import googlemaps

# 地域
regions = ["東京都", "千葉県"]

def extract_next_search_page(current_page_url):
    current_page = requests.get(current_page_url)
    soup = BeautifulSoup(current_page.text, "lxml")
    next_page_div = soup.select(".next")
    if next_page_div:
        return str(next_page_div[0].get("href"))
    else:
        return None
    
def extract_adrresses(target_url):
    page = requests.get(target_url)
    if page.status_code == 200:
        enterprise_infos = []
        soup = BeautifulSoup(page.text, "lxml")
        title_name = "".join(soup.find("title").contents[0])
        target_div = soup.select("#internList > li")
        
        
        # 正規表現
        div_pattern = re.compile(r"勤務先の住所")
        address_pattern = re.compile(r"([" + "".join(regions) + r"].*?)[<>]")
        
        for div in target_div[:1]:
            # タイトルとURLを取得
            title = div.select(".interntitle")[0].contents[0]
            url  = div.select(".interntitle")[0].get("href")

            # URL先に行って住所を取得
            time.sleep(3)
            page = requests.get(url)
            c_soup = BeautifulSoup(page.text, "lxml")
            info_divs = str(c_soup.select(".internInfo")[1])

            address_div_start = re.search(div_pattern, info_divs).start()
            address_part = info_divs[address_div_start:]
            address = re.search(address_pattern, address_part).group(1)
            enterprise_infos.append({\
                "title":   title,\
                "url":     url,\
                "address": address\
            })
        return enterprise_infos
    else:
        return []

if __name__ == "__main__":
    enterprise_infos = []
    search_page = 'http://engineer-intern.jp/?s=&internship=&job=&area=&post_type=intern'

    # スクレイピングで現在の検索ページとそれ以降のページの企業情報を全て取得
    while True:
        enterprise_infos.extend(extract_adrresses(search_page))

        search_page = extract_next_search_page(search_page)
        print(search_page)
        print()
        if not search_page:
            break
    
    # GoogleMap初期化
    geocoder = googlemaps.Client(key='AIzaSyAPO0FiAAXTs6me9JdLxhmZ4FL7kgC26ck')
    gmap = gmplot.GoogleMapPlotter(35.681233, 139.766944, 11)

    # GoogleMapで位置を表示
    for enterprise in enterprise_infos:
        geocode_result = geocoder.geocode(enterprise["address"])
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        gmap.marker(lat, lng, 'red', title=enterprise["title"])

    gmap.draw("my_map.html")
