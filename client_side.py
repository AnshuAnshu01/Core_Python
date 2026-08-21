import socket


def client_program():
    host = socket.gethostname()
    print(host)
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Enter Message Send to Server=")

    while message.lower().strip() != 'stop':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Recieved Message from Server={}'.format(data))
        message = input("Enter Message Send to Server=")

    client_socket.close()


if __name__ == '__main__':
    client_program()
