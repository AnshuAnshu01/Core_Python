import socket


def server_program():
    host = socket.gethostname()
    print(host)
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connected With Client={}".format(str(address)))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Message Received From Client={}".format(str(data)))
        data = input('Enter Message Send to Client=')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()
