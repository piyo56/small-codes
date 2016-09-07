from bs4 import BeautifulSoup
import requests
import re

if __name__ == "__main__":

    # 地域
    regions = ["東京都", "千葉県"]
    search_page = requests.get('http://engineer-intern.jp/?s=&internship=&job=&area=&post_type=intern')

    if search_page.status_code == 200:
        soup = BeautifulSoup(search_page.text, "lxml")
        title_name = "".join(soup.find("title").contents[0])
        target_div = soup.select("#internList > li")
        """
        if title_name == "PyConJP2016":
            target_div = soup.select(".ptype")
            for e in target_div:
                entry_type = e.select(".ptype_name")[0].contents[0]
                acceptance_num = int(e.select(".amount")[1].contents[1].split("/")[1])
                reservation_num = int(e.select(".amount_over")[0].contents[0])
                #print("{0}/{1}".format(reservation_num, acceptance_num))
                if acceptance_num - reservation_num > 0:
                    notify_desktop("{0}の席に空きがでました!!".format(entry_type))
                else:
                    notify_desktop("まだ満員です...".format(entry_type))

        """

    else:
        notify_desktop("PyConJP2016のページソースの取得に失敗しました")
