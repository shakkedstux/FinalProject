#   shakked stux
#   get his screen - "The Visitor" - (server)


# hello
import socket

IP = "0.0.0.0"
PORT = 8820
#qqqqqqqqqqqqqqqqqqqqqqq

def main():
    # connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    friend, address = server_socket.accept()
    
    # receiving and saving image 1 piece at a time
    piece_size = 2000000 # 4 KiB

    with open("copy.jpg", "wb") as out_file:
        piece = friend.recv(piece_size)
        out_file.write(piece)


if __name__ == '__main__':
    main()



# what i did today: 
# git - download all the files. 
# installing Pillow(PIL)
# changing code 'piece_size' to 2 million instead 4096 - so now it works. needs to be changed.. 
# openning 2 files for doing sql homework.
# open another file for creating db and tables
# open db and tables file is working
# tgre2