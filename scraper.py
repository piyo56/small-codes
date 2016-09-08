from bs4 import BeautifulSoup
import requests
import re
import gmplot
import googlemaps

# 地域
regions = ["東京都", "千葉県"]

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
        
        for div in target_div[:2]:
            # タイトルとURLを取得
            title = div.select(".interntitle")[0].contents[0]
            url  = div.select(".interntitle")[0].get("href")

            # URL先に行って住所を取得
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
    enterprise_infos = extract_adrresses('http://engineer-intern.jp/?s=&internship=&job=&area=&post_type=intern')

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
