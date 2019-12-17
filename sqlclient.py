
import socket

IP = '127.0.0.1' # '0.0.0.0' not working
PORT = 8820


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    server_massage = str(client_socket.recv(1000))[1:]
    print("server massge is: " + server_massage)
    name = input("Insert name: ")
    password = input("Insert password: ")

    client_socket.send(("name is " + name).encode())
    client_socket.send(("password is " + password).encode())

    server_massage = str(client_socket.recv(1000))[2:-1]
    
    if(server_massage == "no"): # if no matching user for this name and password
        pass
    else:
        pass


if __name__ == '__main__':
    main()
