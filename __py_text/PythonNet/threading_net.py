from threading import Thread
import sys
from socket import *


def handle(conn_fd):
    print("client: ", conn_fd.getpeername())
    while True:
        data = conn_fd.recv(1024)
        if not data:
            break
        print(data.decode())
        conn_fd.send(b"OK")
    conn_fd.close()


HOST = "0.0.0.0"
PORT = 12016
ADDR = (HOST, PORT)

sock_fd = socket()
sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock_fd.bind(ADDR)
sock_fd.listen(3)

while True:
    try:
        conn, addr = sock_fd.accept()
    except KeyboardInterrupt:
        sys.exit("server exit")
    except Exception as e:
        print(e)
        continue

    t = Thread(target=handle, args=(conn,))
    t.setDaemon(True)  # 主线程退出，分支线程随之退出
    t.start()
