# code from the internet (+clientss.py) - not working fast, when taking screenshot doesn't take the cursor too.(maybe better), pygame.

import socket
from zlib import compress

from mss import mss


WIDTH = 200
HEIGHT = 200


def retreive_screenshot(conn):
    # The region to capture
    rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

    while 'recording':
        # Capture the screen
        img = mss().grab(rect) # this is whats really important
        # Tweak the compression level here (0-9)
        pixels = compress(img.rgb, 6)

        # Send the size of the pixels length
        size = len(pixels)
        size_len = (size.bit_length() + 7) // 8
        conn.send(bytes([size_len]))

        # Send the actual pixels length
        size_bytes = size.to_bytes(size_len, 'big')
        conn.send(size_bytes)

        # Send pixels
        conn.sendall(pixels)


def main(host='0.0.0.0', port=5000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()

    while 'connected':
        retreive_screenshot(conn)


if __name__ == '__main__':
    main()



# need to learn :    SOCKET, DB   - this is all. and then work a lot.