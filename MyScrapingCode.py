from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import time
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

df = pd.DataFrame(columns=['Title', 'Original Price', 'Sale Price', 'Reviews', 'Store', 'URL', 'Page Number', 'Page Location', 'Seller Status', 'Ad Status'])

for page_num in range(1, 6):
    url = f'https://www.etsy.com/search?explicit=1&q=planner&order=most_relevant&page={page_num}&ref=pagination'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    items = soup.find_all("a", {"class": "listing-link"})
    for item in soup.find_all("a", {"class": "listing-link"}):
        row = {}
        try:
            ## Title
            row['Title'] = item.find('h3', {'class': 'wt-text-caption v2-listing-card__title wt-text-truncate'}).text.strip()
            ## Price
            prices = item.find_all('span', {"class": "currency-value"})
            if len(prices) == 1:
                row['Sale Price'] = prices[0].get_text().strip()
                row['Original Price'] = None
            elif len(prices) == 2:
                row['Sale Price'] = prices[0].get_text().strip()
                row['Original Price'] = prices[1].get_text().strip()
            ## Reviews
            row['Reviews'] = item.find('span', {'class': 'wt-text-caption wt-text-gray wt-display-inline-block wt-nudge-l-3 wt-pr-xs-1'}).text.strip()
            ## Store
            store = item.find('p')
            for paragraph in item.find_all('p'):
                if 'aria-label' in paragraph.attrs:
                    if "From shop" in paragraph.attrs['aria-label']:
                        row['Store'] = paragraph.text
            ## URL
            url = item.get('href')
            row['URL'] = url
            ## Page Number
            row['Page Number'] = item.get('data-page-num')
            ## Page Location
            row['Page Location'] = item.get('data-position-num')
            ## Star Seller
            p_tag = item.find('p', {'class': 'wt-text-caption-title wt-nudge-l-2 star-seller-badge-lavender-text-light'})
            if p_tag is not None and 'Star Seller' in p_tag:
                row['Seller Status'] = 'Star Seller'
            else:
                row['Seller Status'] = 'Not a Star Seller'
            # Ad
            ad_badge = item.find('div', {'class': 'wt-text-caption wt-text-truncate wt-text-grey wt-mb-xs-1 min-height'})
            is_ad = ad_badge.find('p')
            if is_ad is not None and is_ad.text == 'Ad vertisement by Etsy seller':
                row['Ad Status'] = 'Ad'
            else:
                row['Ad Status'] = 'Not an Ad'

        except Exception as e:
            # Handle any errors that may occur during extraction
            # raise e
            print(e)
            pass

        df = df.append(row, ignore_index=True)

    time.sleep(5)

print(df)
df.to_csv('test.csv')


