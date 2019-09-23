#!/usr/bin/env python3
from hashlib import md5
from sys import stdin

secret = stdin.readline().strip()

n = 0
while True:
    n += 1
    m = md5()
    m.update(bytes(secret + str(n), 'utf8'))
    digest = m.hexdigest()
    if digest[:5] == '00000':
        break

print(f'{secret} + {n}: {digest}')