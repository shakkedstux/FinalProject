# -*- coding: utf-8 -*-

import socket
from threading import Thread
from zlib import compress
from mss import mss
import math


def show(x):
    try:
        for i in x:
                print("Type = " + str(type(i)) + ", Value = " + str(i))
    except:
        print("Type = " + str(type(x)) + ", Value = " + str(x))


def main():
    """
    Add Documentation here
    """
    # The region to capture
    i = 1000
    rect = {'top': 0, 'left': 0, 'width': i, 'height': i}
    img = mss().grab(rect)
    pixels = compress(img.rgb, 0)
    size = len(pixels)
    size_len = (size.bit_length() + 7) // 8
    print (size)
    print(size_len)
    size_bytes = size.to_bytes(size_len, 'big')
    print(size_bytes)





if __name__ == '__main__':
    main()