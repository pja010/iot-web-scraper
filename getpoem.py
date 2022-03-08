from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://www.poetryfoundation.org/poems/poem-of-the-day')
soup = BeautifulSoup(html_doc.text, 'lxml')

poem = soup.find(class_='c-feature')
print(poem.get_text())