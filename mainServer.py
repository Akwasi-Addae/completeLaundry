import socket
import sqlite3
import threading

login_credentials = {"dendo": "1234"}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9000))
server.listen(5)


def update(connection):
    """
    Receive data.
    Could not figure out how to read transmitted data, so just read what you can to see if it's online or offline
    """

    washer = connection.recv(7)
    status = "OFFLINE"
    stat = connection.recv(2).decode()
    if stat == "ON":
        status = "ONLINE"
    connection.close()

    # Update database
    con = sqlite3.connect("C://Users//kwartd3//djangogirls//db.sqlite3")
    cur = con.cursor()
    print("WasherName: ", washer)
    print("Status: ", status)
    cur.execute(f'''UPDATE example_farrockaway SET Status="{status}" WHERE washerName="{washer.decode()}"''')

    # Save update and terminate connection
    con.commit()
    con.close()


while True:
    print("Listening on port 9000")
    conn, addr = server.accept()

    # Login
    conn.send(b"Username: ")
    username = conn.recv(5).decode()
    conn.send(b"Password: ")
    password = conn.recv(4).decode()

    # Check if username and password are valid
    try:
        login_credentials[username]
    except KeyError:
        print("Username incorrect. Connection aborted\n")
        conn.close()
        continue

    if login_credentials[str(username)] != str(password):
        print("Username or password incorrect. Connection aborted\n")
        conn.send(b'1')
        conn.close()
    else:
        conn.send(b"0")
        print("Accepted connection\n")
        update(conn)
