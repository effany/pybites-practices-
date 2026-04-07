from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')
soup = Soup(CONTENT, 'html.parser')

def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    book = soup.find('div', class_='dotd-main-book')
    summary = soup.find('div', class_='dotd-main-book-summary')
    description = summary.find('div', class_='dotd-title').find_next('div').get_text(strip=True)
    title = summary.find('div', class_="dotd-title").get_text(strip=True)
    img = book.find(class_= 'dotd-main-book-image').find('noscript').find('img')['src']
    book_link = book.find(class_= 'dotd-main-book-image').find('a')['href']
    return Book(title=title, description=description,image=img, link=book_link)
