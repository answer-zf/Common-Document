"""

"""

from socket import *
from threading import Thread
from time import sleep
import os

HOST = "0.0.0.0"
PORT = 12016
ADDR = (HOST, PORT)
FTP = "./ftp/"


class FtpServer:
    """
        服务端操作文件类
        conn_fd: 套接字
        FTP_PATH: 所操作目录地址
            查看目录列表标识符: "L"
            下载文件标识符: "G"
            上传文件标识符: "P"
            退出:"Q"
    """

    def __init__(self, conn_fd, FTP_PATH):
        self.conn_fd = conn_fd
        self.FTP_PATH = FTP_PATH

    # 查询目录文件
    def do_list(self):
        # 判断目录内是否存在文件
        files = os.listdir(self.FTP_PATH)
        if not files:
            self.conn_fd.send("this is empty!".encode())
            return
        else:
            self.conn_fd.send(b"OK")
            sleep(0.1)

        # 避免粘包，采用 \n 做边界，一次发送目录信息
        fs = ""
        for file in files:
            if file[0] != "." and os.path.isfile(self.FTP_PATH + file):
                fs += file + "\n"
        self.conn_fd.send(fs.encode())

    # 下载文件
    def get_file(self, file_name):
        # 通过打开文件是否异常 判断文件是否存在
        try:
            fd = open(self.FTP_PATH + file_name, "rb")
        except Exception:
            self.conn_fd.send(b"File Not Exist")
            return
        else:
            self.conn_fd.send(b"OK")
            sleep(0.1)  # 连续发送,防止粘包

        # 下载文件核心步骤
        while True:
            read_data = fd.read(1024)
            if not read_data:
                sleep(0.1)
                self.conn_fd.send(b"##")
                break
            self.conn_fd.send(read_data)

    # 上传文件
    def put_file(self, file_name):
        # 判断文件是否存在(不允许覆盖文件)
        if os.path.exists(self.FTP_PATH + file_name):
            self.conn_fd.send(b"File Exist")
            return
        self.conn_fd.send(b"OK")
        # 上传核心步骤
        fd = open(self.FTP_PATH + file_name, "wb")
        while True:
            file_data = self.conn_fd.recv(1024)
            if file_data == b"##":
                break
            fd.write(file_data)
        fd.close()


def do_require(conn_fd):
    cls = conn_fd.recv(1024).decode()
    FTP_PATH = FTP + cls + "/"
    ftp = FtpServer(conn_fd, FTP_PATH)
    while True:
        data = conn_fd.recv(1024).decode()
        if not data or data[0] == "Q":
            return
        elif data[0] == "L":
            ftp.do_list()
        elif data[0] == "G":
            file_name = data.split(" ")[-1]
            ftp.get_file(file_name)
        elif data[0] == "P":
            file_name = data.split(" ")[-1]
            ftp.put_file(file_name)


def main():
    sock_fd = socket()
    sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock_fd.bind(ADDR)
    sock_fd.listen(3)
    print("Listen the port 12016 ...")

    while True:
        try:
            conn_fd, addr = sock_fd.accept()
        except KeyboardInterrupt:
            print("server exit")
            return
        except Exception as e:
            print(e)
            continue
        print("Link client: ", addr)

        client = Thread(target=do_require, args=(conn_fd,))
        client.setDaemon(True)
        client.start()


if __name__ == '__main__':
    main()
