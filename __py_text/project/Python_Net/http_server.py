"""
    核心技术点：
        TCP 连接
        SELECT IO 多路复用
        类封装，让用户传递属性 + 重写功能达到 http 实现
"""
from select import select
from socket import *


class HttpServer:
    def __init__(self, server_address, static_dir):
        self.server_address = server_address
        self.static_dir = static_dir
        self.rlist = self.wlist = self.xlist = []
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sock_fd = socket()
        self.sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sock_fd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    def get_html(self, conn_fd, info):
        """
            网页处理
        :param conn_fd:
        :param info:
        :return:
        """
        if info == "/":
            file_name = self.static_dir + "/index.html"
        else:
            file_name = self.static_dir + info
        try:
            fd = open(file_name)
        except Exception:
            response_header = "HTTP/1.1 404 Not Found\r\n"
            response_header += "Content-Type: text/html\r\n"
            response_header += "\r\n"
            response_body = "<h1> Not Found </h1>"
        else:
            response_header = "HTTP/1.1 200 OK \r\n"
            response_header += "Content-Type: text/html\r\n"
            response_header += "\r\n"
            response_body = fd.read()
        finally:
            response_msg = response_header + response_body
            conn_fd.send(response_msg.encode())

    def get_data(self, conn_fd, info):
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Type: text/html\r\n"
        response_header += "\r\n"
        response_body = "<h1> Waiting ... </h1>"
        response_msg = response_header + response_body
        conn_fd.send(response_msg.encode())

    def handle(self, conn_fd):
        """
            http 请求处理
        :param conn_fd: 连接套接字
        :return:
        """
        request = conn_fd.recv(4096)
        # 防止断开
        if not request:
            self.rlist.remove(conn_fd)
            conn_fd.close()
            return
        # 请求解析
        request_line = request.splitlines()[0]
        info = request_line.decode().split(" ")[1]
        if info == "/" or info[-5:] == ".html":
            self.get_html(conn_fd, info)
        else:
            self.get_data(conn_fd, info)

        self.rlist.remove(conn_fd)
        conn_fd.close()

    def server_forever(self):
        self.sock_fd.listen(5)
        print("listen port %d" % self.port)

        self.rlist.append(self.sock_fd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r == self.sock_fd:
                    conn_fd, addr = r.accept()
                    print("connect addr: ", addr)
                    self.rlist.append(conn_fd)
                else:
                    self.handle(r)

            for w in ws:
                pass


if __name__ == '__main__':
    server_address = ("0.0.0.0", 12016)  # 服务器地址
    static_dir = "./static"  # 网页存放位置

    httpd = HttpServer(server_address, static_dir)  # 生成实例化对象
    httpd.server_forever()  # 启动服务
