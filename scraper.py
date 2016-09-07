from bs4 import BeautifulSoup
import requests
import re
import gmplot
import googlemaps

if __name__ == "__main__":
    # gmaps初期化
    geocoder = googlemaps.Client(key='AIzaSyAPO0FiAAXTs6me9JdLxhmZ4FL7kgC26ck')
    gmap = gmplot.GoogleMapPlotter(35.681233, 139.766944, 11)
    lats=[]
    lngs=[]

    # 地域
    regions = ["東京都", "千葉県"]
    search_page = requests.get('http://engineer-intern.jp/?s=&internship=&job=&area=&post_type=intern')

    if search_page.status_code == 200:
        soup = BeautifulSoup(search_page.text, "lxml")
        title_name = "".join(soup.find("title").contents[0])
        target_div = soup.select("#internList > li")
        
        # 郵便番号に一致する正規表現...?
        div_pattern = re.compile(r"勤務先の住所")
        address_pattern = re.compile(r"([" + "".join(regions) + r"].*?)[<>]")
        
        for div in target_div:
            # タイトルとURLを取得
            title = div.select(".interntitle")[0].contents[0]
            link  = div.select(".interntitle")[0].get("href")

            # URL先に行って住所を取得
            page = requests.get(link)
            c_soup = BeautifulSoup(page.text, "lxml")
            info_divs = str(c_soup.select(".internInfo")[1])

            address_div_start = re.search(div_pattern, info_divs).start()
            address_part = info_divs[address_div_start:]
            address = re.search(address_pattern, address_part).group(1)

            # GoogleMapで位置を表示！
            geocode_result = geocoder.geocode(address)
            #lats.append(geocode_result[0]["geometry"]["location"]["lat"])
            #lngs.append(geocode_result[0]["geometry"]["location"]["lng"])
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
            gmap.marker(lat, lng, 'red')
        gmap.draw("my_map.html")
    else:
        pass
