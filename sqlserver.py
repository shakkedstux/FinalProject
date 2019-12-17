
import socket
import sqlite3

IP = "0.0.0.0"
PORT = 8820


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()

    client_socket.send("Insert name and password.".encode())

    client_massage = str(client_socket.recv(1000))
    name = client_massage.split()[2][:-1]  # "'name is x'" -> "x"

    client_massage = str(client_socket.recv(1000))
    password = client_massage.split()[2][:-1]

    if(isInUser(name, password)): # if name and password match a user
        client_socket.send("yes".encode()) # show 'welcome' and products table to the client
    else:
        client_socket.send("no".encode()) # show 'error' to client


def isInUser(name, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.execute("SELECT * from users where name='" + name + "' and password='" + password + "'")
    rows = cursor.fetchall() # type(cursor) is 'sqlite3.Cursor', type(rows) is 'list'
    if len(rows) == 0:
        return False
    return True


if __name__ == '__main__':
    main()

