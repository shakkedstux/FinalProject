from socket import socket
from zlib import decompress

import pygame

WIDTH = 200
HEIGHT = 200



def main(host='127.0.0.1', port=5000):
    sock = socket()
    sock.connect((host, port))
    while True:
        # Retreive the size of the pixels length, the pixels length and pixels
        size_len = int.from_bytes(sock.recv(1), byteorder='big')
        size = int.from_bytes(sock.recv(size_len), byteorder='big')
        pixels = decompress(sock.recv(size))

if __name__ == '__main__':
    main()
