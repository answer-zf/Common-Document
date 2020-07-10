from socket import *

sockfd = socket()
server_addr = ("127.0.0.1", 12016)
sockfd.connect(server_addr)

while True:
    message_client = input("message: ")
    if not message_client:
        break
    sockfd.send(message_client.encode())
    data = sockfd.recv(1024)
    print(data.decode())

sockfd.close()
