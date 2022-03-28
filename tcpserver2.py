import socket
from bs4 import BeautifulSoup
import requests
import random
import threading
import time


html_doc = requests.get('https://www.goodreads.com/quotes')
soup = BeautifulSoup(html_doc.text, 'lxml')

quotes = soup.find_all(class_='quoteText')
quoteList = []

for quote in quotes:
    #print(quote.text)
    quoteList.append(quote.text)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print("Host is: " + host)
port = 50000

serversocket.bind(("", port))
serversocket.listen(5)	# num requests to liste to

clientsocket, addr = serversocket.accept()
print("Connection from " + str(addr))
#msg = "Connected to " + str(host) + " \n"
#clientsocket.send(msg.encode("ascii"))

while True:
    quote = random.choice(quoteList)
    clientsocket.send(quote.encode("utf-8"))
    time.sleep(5)

clientsocket.close()

