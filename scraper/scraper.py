import requests
import bs4

# calling a practice website for people to practice on
base_url = 'http://books.toscrape.com/'
# initializes get request to website
res = requests.get(base_url)
# initializes beautiful soup to format more readable
soup = bs4.BeautifulSoup(res.text, 'lxml')


# collects titles, using alt src because it was was easier than trying to swoop from the title tag
# list that titles will be stored in
book_titles = []

# Looks for images with alt text, which were. Books were the only things with alt image text
titles = soup.select('img', alt=True)

# loops through each book image in the list and appends the title text to the book titles array
for title in titles:
    book_titles.append((title['alt']))

# test to make sure correct data was printing
# print(book_titles)

# collects the price
book_prices = []
prices = soup.select('.price_color')
for price in prices:
    book_prices.append(price.text)

# collects images
book_images = []
images = soup.select('img', src=True)
for image in images:
    image_content = image['src']
    book_images.append(image_content)

