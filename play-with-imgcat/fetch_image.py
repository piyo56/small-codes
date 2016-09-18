#!/usr/bin/env python
#coding:utf-8
import sys
import requests
import json

def write_out(byte_str, name="image"):
    with open(name, "wb") as f:
        f.write(byte_str)

if __name__ == "__main__":
    #request_url = "https://media2.giphy.com/media/Hc8PMCBjo9BXa/200w.gif"
    request_url = "http://vignette4.wikia.nocookie.net/fishwrangler/images/2/23/Suggested_Fish_Wrangler_Favicon.gif/revision/latest?cb=20091118041439" #dummy
    
    r = requests.get(request_url, stream='True')
    sys.stdout.buffer.write(r.raw.read()) 
