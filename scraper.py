from bs4 import BeautifulSoup
import requests
from pync import Notifier

def notify_desktop(msg=""):
    try:
        Notifier.notify(msg, title="PyConJP")
    except:
        pass

if __name__ == "__main__":
    r = requests.get('http://pyconjp.connpass.com/event/30692/')

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        title_name = "".join(soup.find("title").contents[0].split()[:3])
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
        notify_desktop("PyConJP2016のページソースの取得に失敗しました")
