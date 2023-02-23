from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.etsy.com/search?q=planner&ref=pagination&page=2'
r = session.get(url,headers=headers)

r.html.render()
search = r.html.html

# Parse the HTML content of the page with Beautiful Soup
soup = BeautifulSoup(search, 'html.parser')

# Find all the listing titles on the page
listings = soup.find_all('div', {'class': 'v2-listing-card__info'})

for listing in listings:
    title = listing.find('h3', {'class': 'wt-text-caption v2-listing-card__title wt-text-truncate'})
    reviews = listing.find('span',{'class': 'wt-text-caption wt-text-gray wt-display-inline-block wt-nudge-l-3 wt-pr-xs-1'})
    price = listing.find('span',{'class': 'wt-screen-reader-only'})
    print(title.text, reviews)
