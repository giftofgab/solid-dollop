from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.etsy.com/search?q=planner&ref=pagination&page=2'
r = session.get(url)

r.html.render()
search = r.html.html

# Parse the HTML content of the page with Beautiful Soup
soup = BeautifulSoup(search, 'html.parser')
#
# # Find all the listing titles on the page
listings = soup.find_all('div', {'class': 'v2-listing-card__info'})

for listing in listings:
    title = listing.find('h3', {'class': 'v2-listing-card__title'})
    price =
    reviews =
    print(title.text)
# Loop through the titles and print them to the console
# for listing in listings:
#     title = listing.find('h3').
