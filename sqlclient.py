
import socket

IP = '127.0.0.1' # '0.0.0.0' not working
PORT = 8820 # working..


def main():
    # create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    client_socket.connect((IP, PORT))

    # wait to massage from server, and when got it, restore it in variable
    server_massage = str(client_socket.recv(1000))[1:]
    # printing the massage
    print("server massge is: " + server_massage)

    # get name and password from the person
    name = "shakked" # input("Insert name: ")
    password = "aaaa" # input("Insert password: ")

    # send these details to server
    client_socket.send(("name is " + name).encode())
    client_socket.send(("password is " + password).encode())

    # wait to massage from server, and when got it, cuts what is needed and restore it in variable
    server_massage = str(client_socket.recv(1000))[2:-1]

    # process the massage
    if(server_massage == "no"):
        # ( user not exist )
        print("no")
    else:
        # ( user exist )
        print("yes")
        # ???? - need to learn the send() thing
        while True:
            x = client_socket.recv(1000).decode()
            if (x == ""):
                break
            print (x)



if __name__ == '__main__':
    main()
