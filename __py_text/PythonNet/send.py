"""

"""

from socket import *

sock_file = "./sock"
sock_fd = socket(AF_UNIX, SOCK_STREAM)
sock_fd.connect(sock_file)

while True:
    msg = input(">>>")
    if not msg:
        break
    sock_fd.send(msg.encode())
sock_fd.close()
