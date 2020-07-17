"""
    client
"""

from socket import *
import os, sys

# 服务端地址
ADDR = ("127.0.0.1", 12017)


def send_message(sock_fd, name):
    while True:
        try:
            str_input_msg = input("pl. input message: ")
        except KeyboardInterrupt:
            str_input_msg = "quit"
        if str_input_msg == "quit":
            str_send_msg = "Q " + name
            sock_fd.sendto(str_send_msg.encode(), ADDR)
            sys.exit()
        str_send_msg = "C %s %s" % (name, str_input_msg)
        # print(str_send_msg)
        sock_fd.sendto(str_send_msg.encode(), ADDR)


def recv_message(sock_fd):
    while True:
        data, addr = sock_fd.recvfrom(1024)
        if data.decode() == "quit":
            sys.exit()
        print(data.decode() + "\npl. input message: ", end="")


def main():
    sock_fd = socket(AF_INET, SOCK_DGRAM)
    while True:
        str_name = input("pl. input your name: ")
        str_send_info = "L " + str_name
        sock_fd.sendto(str_send_info.encode(), ADDR)
        data, addr = sock_fd.recvfrom(2048)

        if data.decode() == "OK":
            break
        else:
            print(data.decode())

    print("Now You Have Entered Chat Room")

    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_message(sock_fd, str_name)
    else:
        recv_message(sock_fd)


if __name__ == "__main__":
    main()
