from bs4 import BeautifulSoup
from requests_html import HTMLSession

import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.etsy.com/search?q=digital+planner&ref=pagination&page=1'

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')

for item in soup.select('.listing-link'):
    try:
        print('----------------------------------------')
        ## Title
        print(item.select('h3')[0].get_text().strip())
        ## Ads
        print(item.select('p')[4].get_text().strip())
        ## Price
        print(item.select('p')[2].get_text().strip())
        ## Store
        print(item.select('p')[5].get_text().strip())
        ## Stars
        print(item.select('span')[2].get_text().strip())
        ## Reviews
        print(item.select('span')[4].get_text().strip())
        ## URL
        print(item.select('.width-full')[0]['src'])
        ##print(item.select('.currency-value')[0].get_text().strip())
        ##print(item.select('.screen-reader-only')[0].get_text().strip())
        ##print(item.select('.width-full')[0]['src'])
    except Exception as e:
        # Handle any errors that may occur during extraction
        # raise e
        pass





