
import socket
import sqlite3

IP = "0.0.0.0"
PORT = 8820


def myIP():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return IP


def main():
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connecting to client
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()

    # asking for client to send password and name
    client_socket.send("Insert name and password.".encode())

    # getting them (name, password)
    client_massage = str(client_socket.recv(1000))
    name = client_massage.split()[2][:-1]  # "'name is x'" -> "x"

    client_massage = str(client_socket.recv(1000))
    password = client_massage.split()[2][:-1]

    if(isInUser(name, password)): # if name and password match a user
        client_socket.send("yes".encode()) # let the client know
        products = getProductsList() # send the products
        for i in products:
            for j in i:
                client_socket.send(str(j).encode())
        client_socket.send("done".encode()) # let the client know
    else:
        client_socket.send("no".encode()) # let the client know


def getProductsList():
    conn = sqlite3.connect('user.db') # is it neceaary (did it already)
    cursor = conn.execute("SELECT * from products")
    rows = cursor.fetchall() # type(cursor) is 'sqlite3.Cursor', type(rows) is 'list' - ??? - but working..
    return(rows)


def isInUser(name, password):
    # connecting to data base
    conn = sqlite3.connect('user.db') # is it neceaary (did it already)

    # takes information from the data base (from a table in the data base)
    cursor = conn.execute("SELECT * from users where name='" + name + "' and password='" + password + "'")

    rows = cursor.fetchall() # type(cursor) is 'sqlite3.Cursor', type(rows) is 'list' - ??? - but working..
    if len(rows) == 0:
        return False
    return True


if __name__ == '__main__':
    main()

