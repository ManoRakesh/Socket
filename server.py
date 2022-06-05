# server.py
import sockect
#1 
s = socket.socket()
host = socket.gethostname()
port = 1234
#2
s. bind((host,port))
#3
s.listen(5)
#4
while True:
    conn, addr = s.accept()
    print("Got connection from :",addr)
    conn.send(b 'Thank you for connecting')
    conn.close()