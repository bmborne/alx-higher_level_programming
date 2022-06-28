#!/usr/bin/python3
for i in range(0, 99):
    if i == 98:
        print("{}\n".format(i))
    else:
        print("{:0=2d}".format(i), end=", ")
