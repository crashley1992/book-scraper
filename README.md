# book-scraper
Purpose: 
The purpose of this app was to build a web scraper that is able to pull information from a dummy site for practicing web scraping called http://books.toscrape.com/. Once the data is collected by the scraper, it updates in the MySQL Workbench server. There were some constraints from using this website to scrape. One being that author information wasn't available. 


How to run it:
1. Make sure that you have MySQL WorkBench running. Update the passwords and user info with your own in the config and connection files.
2. Build a table in SQL that will hold the book info. Here is an example of what mine looks like:
CREATE DATABASE books;

USE books;

CREATE TABLE BOOKS_LIST (
    Book_ID int,
    Book_Title varchar(100),
    BOOK_PRICE varchar(100),
    Book_image varchar(255)
)

3. In the scraper.py file, adjust the Book_List table to whatever you named yours in SQL. That goes for the column names as well.
4. Run the scraper.py file in your terminal and the tables should update. You can adjust this line of code to add more or different books. 

def main():
   insert_book(book_titles[1], book_prices[1])



Technologies used:
Python
MySQL WorkBench

Python Packages:
- requests
- bs4 (beautiful soup)
- mysql-connector-python

