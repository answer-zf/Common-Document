from socket import *
import os, sys
import signal


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

# 创建监听套接字
sock_fd = socket()
sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口的重用
sock_fd.bind(ADDR)
sock_fd.listen(3)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("listen 12016")

while True:
    try:
        conn_fd, addr = sock_fd.accept()
    except KeyboardInterrupt:
        sys.exit("server exit")
    except Exception as e:
        print(e)
        continue

    pid = os.fork()

    if pid == 0:
        sock_fd.close()
        handle(conn_fd)
        os._exit(0)
    else:
        conn_fd.close()
