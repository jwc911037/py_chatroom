import socket
import select
# from _thread import *

if __name__ == '__main__':
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5000
    HOST = ''

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    CONNECTION_LIST.append(server_socket)

    print('Chat server has started on port: '+ str(PORT))

    def broadcast_toall(sock, message):
        for s in CONNECTION_LIST:
            if s == sock:
                continue
            sock.send(message.encode())

    while True:

        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
      
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print('Client (%s, %s) connected' % addr)
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        sock.send(data)
                        print(data.decode())
                except:
                    broadcast_toall(sock, 'Client (%s, %s) is offline' % addr)
                    print('Client (%s, %s) is offline' % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    server_socket.close()

