import socket

NUM_BYTES = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000

sock.connect((host, port))
msg = sock.recv(NUM_BYTES)	
sock.close()
print(msg.decode('ascii'))
