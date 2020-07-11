"""

"""

import os

pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("child pid", os.getpid())
    os._exit(2)
else:
    pid, status = os.wait()
    print("pid", pid)
    print("status", status)  # 2 x 256 / os.WEXITSTATUS() => 2
    while True:
        pass
