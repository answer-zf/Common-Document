"""
    TCP 套接字 客户端
"""

from socket import *

sockfd = socket()

server_addr = ("127.0.0.1", 12016)

sockfd.connect(server_addr)

sockfd.send(b"answer-zf")

data = sockfd.recv(1024)

print(data.decode())

sockfd.close()
