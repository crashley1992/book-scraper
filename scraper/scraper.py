import requests
import bs4

# calling a practice website for people to practice on
base_url = 'http://books.toscrape.com/'
# initializes get request to website
res = requests.get(base_url)
# initializes beautiful soup to format more readable
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)

