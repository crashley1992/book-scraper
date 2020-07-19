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


# imports file used for connection and used mysql.connector package to establish connection to sql server
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

# function that inserts book title and book price into sql table
def insert_book(Book_Title, BOOK_PRICE):
    query = "INSERT INTO BOOKS_LIST(Book_Title,BOOK_PRICE) " \
            "VALUES(%s,%s)"
    args = (Book_Title, BOOK_PRICE)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
   insert_book(book_titles[1], book_prices[1])

if __name__ == '__main__':
    main()