from socket import *
from time import sleep
import sys


class FtpClient:
    """
        客户端操作文件类
        sock_fd: 套接字
            查看目录列表标识符: "L"
            下载文件标识符: "G"
            上传文件标识符: "P"
            退出:"Q"
    """

    def __init__(self, sock_fd):
        self.sock_fd = sock_fd

    # 查询目录列表
    def do_list(self):
        self.sock_fd.send(b"L")
        data = self.sock_fd.recv(128).decode()
        if data == "OK":
            request_msg = self.sock_fd.recv(4096)
            print(request_msg.decode())
        else:
            print(data)

    # 下载文件
    def get_file(self, filename):
        self.sock_fd.send(("G " + filename).encode())
        recv_signal = self.sock_fd.recv(128).decode()
        if recv_signal == "OK":
            # 下载文件核心步骤
            fd = open(filename, "wb")
            while True:
                recv_data = self.sock_fd.recv(1024)
                # 服务端不会发空，需要结束标志
                if recv_data == b"##":
                    break
                fd.write(recv_data)
            fd.close()
        else:
            print(recv_signal)

    # 上传文件
    def put_file(self, file_url):
        # 通过异常做文件判断
        try:
            fd = open(file_url, "rb")
        except Exception:
            print("file name exist, pl. input again!")
            return
        # 避免将路径上传到服务端
        file_name = file_url.split("/")[-1]

        self.sock_fd.send(("P " + file_name).encode())
        recv_signal = self.sock_fd.recv(128).decode()
        if recv_signal == "OK":
            # 上传文件核心步骤
            while True:
                send_data = fd.read(1024)
                if not send_data:
                    sleep(0.1)
                    self.sock_fd.send(b"##")
                    break
                self.sock_fd.send(send_data)
            fd.close()
        else:
            print(recv_signal)

    def do_quit(self):
        self.sock_fd.send(b"Q")
        self.sock_fd.close()
        sys.exit("Thanks to use")


def do_request(sock_fd):
    ftp = FtpClient(sock_fd)

    while True:
        print("\n======== Command  Options ========")
        print("************** list **************")
        print("************ get file ************")
        print("************ put file ************")
        print("************** quit **************")
        print("==================================")

        cmd = input("pl. input command : ")
        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd.strip() == "quit":
            ftp.do_quit()
        elif cmd.strip()[:3] == "get":
            file_name = cmd.split(" ")[-1]
            ftp.get_file(file_name)
        elif cmd.strip()[:3] == "put":
            file_name = cmd.split(" ")[-1]
            ftp.put_file(file_name)


def main():
    addr = ("127.0.0.1", 12016)
    sock_fd = socket()
    try:
        sock_fd.connect(addr)
    except Exception as e:
        print("Server Connect Error")
        return
    else:
        print("""
            ************************
               Data  Image  File
            ************************
        """)
        cls = input("pl. input document type: ")
        if cls not in ["Data", "Image", "File"]:
            print("input Error!")
            return
        else:
            sock_fd.send(cls.encode())
            do_request(sock_fd)


if __name__ == '__main__':
    main()
