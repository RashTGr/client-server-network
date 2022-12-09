# Setup the Server socket

import socket

import threading


# Parameters for configuring the 'Server' socket
# getting local machine name
HOST = socket.gethostbyname(socket.gethostname())
# reserving a free port for network
PORT = 17000    
addr = (HOST, PORT)
# setting byte limit for send/receive data
header = 64
# message to handle disconnections
connect_status = "..!TERMINATED"

# Create a server socket and bind it to the address
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(addr)


def connect(conn, addr):
    """Manage connections between server and client."""
    
    # Notification on successful connections
    print(f"_CONNECTED_ client addr: {addr} ")
    
    # Receive deserialised data within the allotted bytes
    connected = True
    while connected:
        data_size = conn.recv(header).decode("utf-8")
        if data_size: 
            data_size = int(data_size)
            data = conn.recv(data_size).decode("utf-8")
            
            # Handle client disconnection 
            if data == connect_status:
                connected = False
            print(f"[{addr}] {data}")

            # Delivery message to client
            conn.send("Delivered!".encode("utf-8"))
    conn.close()


def listen():
    """Start listening for connections and pass it to 
    'connect' function for processing.
    """
    serv.listen(5)
    print(f"[LISTENING..] host: {HOST}")
    while True:
        conn, addr = serv.accept()

        # To keep track of current users connected
        # !This method works with Python 3 versions only
        thread = threading.Thread(target=connect, args=(conn, addr))
        thread.start()
        print(f"active clients: _ {threading.active_count()- 1}")

# Start listening
listen()