#!/usr/bin/env python3

import sys
from pwn import *

if sys.version_info.major == 2:
    print("Menace, Menace!!!!")
    print("Run it with python3")

k1 = bytes.fromhex(sys.argv[1])
k2_3 = bytes.fromhex(sys.argv[2])
flag = bytes.fromhex(sys.argv[3])

print("Here is the flag:")
print(xor(k1,k2_3,flag))
