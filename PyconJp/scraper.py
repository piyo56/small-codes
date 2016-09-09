from bs4 import BeautifulSoup
import requests
from pync import Notifier

r = requests.get('http://pyconjp.connpass.com/event/30692/')

flag = False

# GET response status
if r.status_code == 200:
    soup = BeautifulSoup(r.text, "lxml")
    target_div = soup.select(".ptype")
    #title_name = "".join(soup.find("title").contents[0].split()[:3])
    #if title_name == "PyConJP2016":
    
    # 応募種類から予約数と受け入れ数を取得
    for e in target_div:
        entry_type = e.select(".ptype_name")[0].contents[0]
        acceptance_num = int(e.select(".amount")[1].contents[1].split("/")[1])
        reservation_num = int(e.select(".amount_over")[0].contents[0])
        #print("{0}/{1}".format(reservation_num, acceptance_num))

        if acceptance_num - reservation_num > 0:
            flag = True
            Notifier.notify("{0}の席に空きがでました!!".format(entry_type), title="PyConJP2016")

    if flag:
        Notifier.notify("まだ満員です...", title="PyConJP2016")

else:
    Notifier.notify("PyConJP2016のページソースの取得に失敗しました", title="PyConJP2016")
