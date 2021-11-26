#!/usr/bin/env python3

import sys
from pwn import *

if sys.version_info.major == 2:
    print('Run it with Python3')

byte_t = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

print('Here is the flag:')
#print(xor(byte_t, 'crypto{'.encode()))
print(xor(byte_t, 'myXORkey'.encode()))
