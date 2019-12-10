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
    piece_size = 4096 # 4 KiB

    with open("copy.jpg", "wb") as out_file:
        while True:
            piece = friend.recv(piece_size)

            if piece == "":
                break # end of file

            out_file.write(piece)


if __name__ == '__main__':
    main()