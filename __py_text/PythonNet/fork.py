"""
    fork
"""
import os

pid = os.fork()

if pid < 0:
    print("Create Process Failed")
elif pid == 0:
    print("the new process")
else:
    print("the old process")

print("fork test over")
