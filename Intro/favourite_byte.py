#!/usr/bin/env python3

import sys
from  pwn import *

if sys.version_info.major == 2:
    print('Run it python3')

hex_t = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

print("Here is the flag:")
for i in range(0, 256):
    print(f"key:{i}  {xor(hex_t, i)}") 
