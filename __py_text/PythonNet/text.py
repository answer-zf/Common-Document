"""

"""

from socket import *
from select import select

sock_fd = socket()
sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock_fd.bind(("0.0.0.0", 12016))
sock_fd.listen(3)

rlist = [sock_fd]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sock_fd:
            conn_fd, addr = sock_fd.accept()
            print("Connect From", addr)

            rlist.append(conn_fd)  # 加入新的关注IO
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b"OK")
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)
    for x in xs:
        pass
