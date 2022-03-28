from bs4 import BeautifulSoup
import requests
import random

html_doc = requests.get('https://www.goodreads.com/quotes')
soup = BeautifulSoup(html_doc.text, 'lxml')

quotes = soup.find_all(class_='quoteText')
quoteList = []

for quote in quotes:
    #print(quote.text)
    quoteList.append(quote.text)

quote = random.choice(quoteList)
print(quote)
