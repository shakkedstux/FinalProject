import socket


def main(host='127.0.0.1', port=5000):
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect((host, port))


if __name__ == '__main__':
    main()