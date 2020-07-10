"""
    server
"""

import struct
from socket import *

sock_fd = socket(AF_INET, SOCK_DGRAM)

sock_fd.bind(("0.0.0.0", 12016))

st = struct.Struct("i32sif")
file_desc = open("struct.txt", "a")

while True:
    data, addr = sock_fd.recvfrom(1024)
    tuple_write_msg = st.unpack(data)
    write_msg = "%d %s %d %.2f\n" % (tuple_write_msg[0],
                                     tuple_write_msg[1].decode(),
                                     tuple_write_msg[2],
                                     tuple_write_msg[3])
    file_desc.write(write_msg)
    file_desc.flush()

file_desc.close()
sock_fd.close()
