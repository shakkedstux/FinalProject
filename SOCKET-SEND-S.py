import socket

def main(host='0.0.0.0', port=5000):
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.bind((host, port))
    x.listen(5)
    conn, addr = x.accept()

    while True:
        conn.recv(233)
        print("a")



if __name__ == '__main__':
    main()