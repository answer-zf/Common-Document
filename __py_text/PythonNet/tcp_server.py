"""
    TCP套接字 服务端
"""

import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.bind(("0.0.0.0", 12016))

sockfd.listen(3)

print("waiting for connect...")

connfd, addr = sockfd.accept()

data = connfd.recv(1024)

print("receive message", data)

n = connfd.send(b"Receive message")

print("send", n)

connfd.close()
sockfd.close()
