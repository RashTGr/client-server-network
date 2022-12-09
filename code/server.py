# Creating server

import socket

import threading

Port = 17000
Server = socket.gethostbyname(socket.gethostname())
addr = (Server, Port)
header = 64


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding socket to the address
server.bind(addr)

# Manage the connection between server and client
def handle_client(conn, addr):
    print(f"[CONNECTED].. connection to {addr} successful")

    connected = True
    while connected:
        # msg_len = conn.recv(header).decode("utf-8")
        # if msg_len:
        #     msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode("utf-8")

            # To handle client disconnection 
            # if msg == "!Disconnected":
            #     connected = False

            print(f"[{addr}] {msg}")
    conn.close()


def start():
    """For server to start listening for connections and 
    pass it to 'handle client' function for processing.
    """
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.active_count()}")




# # Create socket for the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Using the method for server/client are on the same machine
# s.bind((socket.gethostname(), 1700))

# # Create listen method
# s.listen(5)

# while True:
#     clt, adr = s.accept()
#     print(f"Connection to {adr} established")
#     clt.send(bytes("Client-Server network programming in Python", "utf-8"))
#     clt.close()