#coding: utf-8
import sys
import time
import json
from bs4 import BeautifulSoup
import requests
import re
import googlemaps
import gmplot

def print_error(msg):
    print("----> [Error] {}".format(msg))
    sys.exit()

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

if __name__ == "__main__":
    print("start scraping...")
    company_infos = []
    count = 0
    head_url = "https://www.wantedly.com"
    search_page_url = 'https://www.wantedly.com/search?_=1473480627140&h=internship&l=kanto&o=web_engineer&page=2&t=projects'
    
    regions = ["東京都", "千葉県", "埼玉県", "茨城県", "神奈川県"]
    load_more = True
    address_pattern = re.compile(r"(((" + r"|".join(regions) + r").*?[0-9０-９-丁目]+).*?)")
    
    # 次のページがなくなるまで
    while load_more:
        print("\n\t- {}".format(search_page_url))
        search_page_soup = fetch_page_source(search_page_url)
        if search_page_soup is None:
            sys.exit()
        
        # 検索でヒットした企業
        target_div = search_page_soup.select(".result-group > a")
        if not len(target_div):
            print_error("search_page is not valid")

        # 各企業（プロジェクト）に対し
        for d in target_div:
            company = {"name":"", "title":"", "url":"", "addr":""}

            company["url"] = head_url + d.get("href")
            project_page_soup = fetch_page_source(company["url"])
            if project_page_soup is None:
                continue

            # 募集タイトル、会社名、url、住所を取得
            try:
                company["name"]  = project_page_soup.select(".wt-company")[0].contents[0].strip()
                company["title"] = project_page_soup.select(".project-title")[0].contents[0].strip()
                #tmp = project_page_soup.select(".address")[0].contents[0].strip()
                #company["addr"]  = re.search(address_pattern, tmp).group(2)
                company["addr"] = project_page_soup.select(".address")[0].contents[0].strip().split(" ")[0]

            except Exception as e:
                print_error("faild to extract project info (exception:{})".format(type(e)));
                continue

            company_infos.append(company)
            print("\t\t* "+company["name"])
        
        # 次のページがあればsearch_page_urlを更新してループ
        try:
            search_page_url = search_page_soup.select(".load-more")[0].contents[1].get("href")
            search_page_url = head_url + search_page_url
        except:
            load_more = False
        
    # GoogleMap初期化
    print("plotting Google Map...")
    geocoder = googlemaps.Client(key='AIzaSyAPO0FiAAXTs6me9JdLxhmZ4FL7kgC26ck')
    gmap = gmplot.GoogleMapPlotter(35.681233, 139.766944, 11) #東京駅を中心に

    # GoogleMapで位置を表示
    for company in company_infos:
        geocode_result = geocoder.geocode(company["addr"])
        if not geocode_result or len(geocode_result) == 0:
            print_error("failed to geocode (url:{})".format(company["url"]))
            continue

        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        gmap.marker(lat, lng, 'red', title=company["name"])

    print("writing out as my_map.html...")
    gmap.draw("my_map.html")
    print("\ndone")
