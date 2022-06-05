
import socket
#1
s = socket.socket()
host = socket.gethostname()
port = 1234
#2
s.connect((host,port))
print(s.recv(1024))
s.close()