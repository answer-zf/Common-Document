"""

"""

from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ("0.0.0.0", 12016)
sockfd.bind(server_addr)

while True:
    data, addr = sockfd.recvfrom(5)
    print("receive: ", data.decode())
    sockfd.sendto(b"answer-zf", addr)
sockfd.close()
