#!/usr/bin/env python3

import sys 
import base64

if sys.version_info.major == 2:
    print("HEYYY!! Run it with Python3")

hex_t = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex_to_byte = bytes.fromhex(hex_t)

print("Here is the flag:")
print(base64.b64encode(hex_to_byte))
