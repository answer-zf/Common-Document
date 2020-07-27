"""

"""
# gevent 协程 TCP

from socket import *
import gevent
from gevent import monkey

monkey.patch_all()

sock_fd = socket()
sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock_fd.bind(("0.0.0.0", 12016))
sock_fd.listen(3)


def handle(conn_fd):
    while True:
        data = conn_fd.recv(1024)
        if not data:
            break
        print(data.decode())
        conn_fd.send(b"OK")
    conn_fd.close()


while True:
    conn_fd, addr = sock_fd.accept()
    print("connect ... ", addr)
    # handle(conn_fd)  # 循环方案
    gevent.spawn(handle, conn_fd)  # 协程方案

sock_fd.close()
