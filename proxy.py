import requests
from bs4 import BeautifulSoup
import pandas as pd


http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

data = {'Title' : {}, 'price' : {}}

url = "https://www.amazon.in/s?k=iphone&crid=2RR0EWSI9T1A5&sprefix=%2Caps%2C209&ref=nb_sb_ss_recent_1_0_recent"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url, headers=headers)


soup  = BeautifulSoup(r.text, 'html.parser')

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")

for span in spans:
    print(span.string)
    #data["Title"].append(span.string)
    
for price in prices: 
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        #data["price"].append(price.find("span").get_text())
        ##   break
        
#df = pd.DataFrame.from_dict(data)        
#df.to_excel("data.xlsx", index = False)