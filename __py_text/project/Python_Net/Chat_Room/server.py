"""
    server
"""

from socket import *
import os, sys

# 地址
ADDR = ("0.0.0.0", 12017)

# 用户信息
dict_user_info = {}


def do_quit(sock_fd, name):
    str_msg = "%s out chat room" % name
    for item in dict_user_info:
        if item != name:
            sock_fd.sendto(str_msg.encode(), dict_user_info[item])
        else:
            sock_fd.sendto(b"quit", dict_user_info[item])
    # 删除用户信息
    del dict_user_info[name]


def do_chat(sock_fd, name, msg):
    str_send_msg = "\n%s : %s" % (name, msg)
    for item in dict_user_info:
        if item != name:
            sock_fd.sendto(str_send_msg.encode(), dict_user_info[item])


def do_login(sock_fd, name, addr):
    if name in dict_user_info or "admin" in name:
        sock_fd.sendto(b"\nNAME EXIST", addr)
        return

    # 发送返回信息
    sock_fd.sendto(b"OK", addr)
    # 记录用户信息
    dict_user_info[name] = addr

    # 向其他用户发送通知
    send_msg = "\nWelcome to %s enter chat room" % name
    for item in dict_user_info:
        if item != name:
            sock_fd.sendto(send_msg.encode(), dict_user_info[item])


def do_request(sock_fd):
    while True:
        data, addr = sock_fd.recvfrom(1024)
        list_recv_info = data.decode().split(" ")
        if list_recv_info[0] == "L":
            do_login(sock_fd, list_recv_info[1], addr)
        elif list_recv_info[0] == "C":
            chat_msg = " ".join(list_recv_info[2:])
            do_chat(sock_fd, list_recv_info[1], chat_msg)
        elif list_recv_info[0] == "Q":
            if list_recv_info[1] not in dict_user_info:
                sock_fd.sendto(b"quit", addr)
                continue
            do_quit(sock_fd, list_recv_info[1])


def super_admin_rights(sock_fd):
    """
        超级管理员发言
            核心：由于子进程的数据 父进程不能共享
                采用 父进程像客户端一样，向子进程发送消息，
                    子进程统一处理请求的方案解决
    :param sock_fd:
    :return:
    """
    while True:
        str_msg = input("admin message: ")
        str_admin_msg = "C admin " + str_msg
        sock_fd.sendto(str_admin_msg.encode(), ADDR)


def main():
    sock_fd = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址
    sock_fd.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        # 处理请求
        do_request(sock_fd)
    else:
        super_admin_rights(sock_fd)


if __name__ == "__main__":
    main()
