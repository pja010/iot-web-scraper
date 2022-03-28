import socket
from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://www.poetryfoundation.org/poems/poem-of-the-day')
soup = BeautifulSoup(html_doc.text, 'lxml')
poem = soup.find(class_='c-feature')

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print("Host is: " + host)
port = 50000

serversocket.bind(("", port))
serversocket.listen(5)	# num requests to liste to

while True:
    clientsocket, addr = serversocket.accept()
    print("Connection from " + str(addr))
    msg = "Connected to " + str(host) + " \n"
    clientsocket.send(msg.encode("ascii"))
    
    msg = poem.get_text()
    clientsocket.send(msg.encode("ascii"))

    clientsocket.close()
