import sys
import time
from bs4 import BeautifulSoup
import requests
from pync import Notifier


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
    soup = fetch_page_source('http://pyconjp.connpass.com/event/30692/')

    if soup is not None:
        fully_occupied = True
        target_div = soup.select(".ptype")
        print(len(target_div))

        # 応募種類から予約数と受け入れ数を取得
        for e in target_div:
            try:
                entry_type      = e.select(".ptype_name")[0].contents[0]
                acceptance_num  = int(e.select(".amount")[1].contents[1].split("/")[1])
                reservation_num = int(e.select(".amount_over")[0].contents[0])
                print("{}:{}/{}".format(entry_type, reservation_num, acceptance_num))
                # 空きがあれば通知
                if acceptance_num - reservation_num > 0:
                    fully_occupied = False
                    Notifier.notify("{0}の席に空きがでました!!".format(entry_type), title="PyConJP2016")
            except Exception as e:
                print("({} ---> {})".format(entry_type, e.args[0]))
                continue

        if fully_occupied:
            Notifier.notify("まだ満員です...", title="PyConJP2016")
    else:
        Notifier.notify("PyConJP2016のページソースの取得に失敗しました", title="PyConJP2016")
