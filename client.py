import socket
import sys

try:
    #using ipv4, TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error:
    print('Failed to connect')
    sys.exit()

# print('Socket Created')
host = 'www.google.com'
port = 80

# Turn hostname into ip
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()
# print(remote_ip)

# connect to google
s.connect((remote_ip, port))

# send a message to google
message = "GET / HTTP/1.1\r\n\r\n"
try:
	s.sendall(message.encode())
except socket.error:
	print('Did not send successfully')
	sys.exit()

# get a reply from google
reply = s.recv(4096) #4096bytes
print(reply.decode())

# close the socket
s.close()

