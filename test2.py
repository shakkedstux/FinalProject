# -*- coding: utf-8 -*-


def main(host='0.0.0.0', port=5000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()

    while 'connected':
        retreive_screenshot(conn)

if __name__ == '__main__':
    main()