#   shakked stux
#   send your screen - "The One Who Needs Help" - (client)

import socket
from PIL import ImageGrab

#test

IP = '127.0.0.1' # '0.0.0.0' not working
PORT = 8820


def main():
    # connection
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.connect((IP, PORT))

    # save screenshot
    im = ImageGrab.grab()
    im.save(r'D:\Users\Cyber\Downloads\screenshot.jpg')    print("screenshot saved")
    # send the image 1 piece at a time
    piece_size = 4096 # 4 KiB

    with open("screenshot.jpg", "rb") as in_file:
        while True:
            piece = in_file.read(piece_size)
            if piece == "":
                break # end of file
            sockt.send(piece)


if __name__ == '__main__':
    main()