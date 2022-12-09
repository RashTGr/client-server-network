# Creating server

import socket

import threading

Port = 17000
Server = socket.gethostbyname(socket.gethostname())
addr = (Server, Port)
header = 64
conn_status = "..!TERMINATED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding socket to the address
server.bind(addr)

# Manage the connection between server and client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION].. connection to {addr} successful")

    connected = True
    while connected:
        msg_length = conn.recv(header).decode("utf-8")
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            
            # To handle client disconnection 
            if msg == conn_status:
                connected = False

            print(f"[{addr}] {msg}")

            # Delivery message to client
            conn.send("Delivered!".encode("utf-8"))
        
    conn.close()


def start():
    """For server to start listening for connections and 
    pass it to 'handle client' function for processing.
    """
    server.listen()
    print(f"[LISTENING] Server is listening on {Server}")
    while True:
        conn, addr = server.accept()

        # To keep track of current users connected
        # !This method works with Python 3 versions
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"CLIENTS:_ {threading.active_count()- 1}")

start()


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