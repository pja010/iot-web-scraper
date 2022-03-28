import socket

NUM_BYTES = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000

sock.connect((host, port))
msgs = []

while True:
    msg = sock.recv(NUM_BYTES)	
    if len(msg) == 0:
        break
    msgs.append(msg.decode('utf-8'))
    print("".join(msgs[-1]))

sock.close()
#print("".join(msgs))

