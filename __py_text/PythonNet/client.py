"""
    client
"""

from socket import *
import struct

sock_fd = socket(AF_INET, SOCK_DGRAM)

ADDR = ("127.0.0.1", 12016)
st = struct.Struct("i32sif")

while True:
    print("====================")
    input_id = int(input("user id: "))
    input_name = input("user name: ").encode()
    input_age = int(input("user age: "))
    input_score = float(input("user score: "))
    send_msg = st.pack(input_id, input_name, input_age, input_score)
    sock_fd.sendto(send_msg, ADDR)

sock_fd.close()
