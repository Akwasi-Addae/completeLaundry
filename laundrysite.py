import socket
import threading


def handle_client(connection, main_socket):
    main_socket.send(connection.recv(7))
    main_socket.send(connection.recv(2))
    print("Data sent\n")
    connection.close()
    main_socket.close()


server = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 10000
server.bind(("127.0.0.1", port))
server.listen(4)

while True:
    print("Listening on port {}".format(port))
    conn, addr = server.accept()
    print("Connection established")

    # Connect to the main server
    main_server = socket.socket()
    main_server.connect(("127.0.0.1", 9000))

    # Username
    main_server.recv(9)
    main_server.send(b"dendo")

    # Password
    main_server.recv(9)
    main_server.send(b"1234")

    if main_server.recv(1).decode() == "P":
        print("Connection to Main Server Successfully Established!")
        client_handler = threading.Thread(target=handle_client, args=(conn, main_server))
        client_handler.start()
    else:
        print("Connection to Main Server Failed")
        main_server.close()
