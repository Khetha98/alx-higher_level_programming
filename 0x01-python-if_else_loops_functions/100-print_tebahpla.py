#!/usr/bin/python3

for j in range(ord('z'), ord('a') - 1, -1):
    if j % 2 == 0:
        d = 0
    else:
        d = 32
    print("{}".format(chr(j - d)), end="")
