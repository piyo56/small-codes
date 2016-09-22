#coding: utf-8
"""
簡単なWebクローラの構築
ref: http://nwpct1.hatenablog.com/entry/python-search-engine
"""
import sys, time

def fetch_page(url):
    """
    ページソースからコンテンツを取得する
    """
    try
        import requests
        time.sleep(1)
        target_page = requests.get(url)
        return target_page.text
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0    
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break


if __name__ == "__main__":
    url = "http://dotinstall.com/lessons"
    page = fetch_page(url)
    print_all_links(page)
