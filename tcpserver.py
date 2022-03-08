import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000

serversocket.bind((host, port))
serversocket.listen(5)	# num requests to liste to

while True:
    clientsocket, addr = serversocket.accept()
    print("Connection from " + str(addr))
    msg = "Connected to " + str(host) + " \n"
    clientsocket.send(msg.encode("ascii"))
    clientsocket.close()
