import socket
import sys
from _thread import *

host = ''
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error:
    print('Binding failed')
    sys.exit()

s.listen(10) #up to 10 peeople can send the msg
print('Socket is ready')

def clientthread(conn):
    welcomemsg = 'Welcome to the server. Type something and hit ENTER.\n'
    conn.send(welcomemsg.encode())
    while True:
        data = conn.recv(1024)
        if not data:
            break;
        print(data.decode())
        # conn.sendall(data)
    conn.close()

# conn, addr = s.accept()
# print('Connect with '+ addr[0]+':'+str(addr[1]))

# while True:
#     data = conn.recv(1024)
#     conn.sendall(data)
#     print(data)

# conn.close()
while True:
    conn, addr = s.accept()
    print('Connect with '+ addr[0]+':'+str(addr[1]))
    start_new_thread(clientthread, (conn,))
s.close()