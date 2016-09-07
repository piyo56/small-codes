from bs4 import BeautifulSoup
import requests
import lxml

r = requests.get('http://pyconjp.connpass.com/event/30692/')

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "lxml")
    print(soup.title())
    target_div = soup.select(".ptype")
    for e in target_div:
        acceptance_num = e.select(".amount")[1].contents[1].split("/")[1]
        reservation_num = e.select(".amount_over")[0].contents[0]
        #print("{0}/{1}".format(reservation_num, acceptance_num))
else:
    #エラーの旨をhogehoge
    pass

# soup = BeautifulSoup(html, "lxml")
# print(soup)
