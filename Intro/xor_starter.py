#!/usr/bin/env python3

import sys
from pwn import *

if sys.version_info.major == 2:
    print("HEEYYYYY MENACE MENACE ATTACHÉ VOS CEINTURES!!!!")
    print("Run it with Python3")

print("Here is the flag:")
print(xor(b'label',13))
