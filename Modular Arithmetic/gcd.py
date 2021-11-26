#!/usr/bin/env python3

def gcd(a,b):
    if b == 0:
        print(a)
    else:
        print(gcd(b,a%b))
gcd(81,57)
