import sys
import time
from bs4 import BeautifulSoup
import requests
import re
import gmplot
import googlemaps

def print_error(msg):
    print("----> [Error] {}".format(msg))
    sys.exit()

if __name__ == "__main__":
    print("start scraping...")
    company_names = []
    count = 0
    url = 'https://www.wantedly.com/search?_=1473480627140&h=internship&l=kanto&o=web_engineer&page=2&t=projects'
    
    load_more = True
    while load_more:
        print("\t- "+url)

        # ページソースを取得
        target_page = requests.get(url)
        soup = BeautifulSoup(target_page.text, "lxml")
        
        # 検索にヒットした企業名を取得
        target_divs = soup.select(".company-name")
        if not len(target_divs):
            print_error("input url is not valid")
        company_names.append(map(lambda div:div.contents[0].strip(), target_divs))
        
        try:
            url = soup.select(".load-more")[0].contents[1].get("href")
            url = "https://www.wantedly.com" + url
        except:
            load_more = False
            
        time.sleep(2)

