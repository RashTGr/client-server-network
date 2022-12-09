# Setup the Client socket

import socket


# Parameters for configuring the 'Client' socket
# getting local machine name
HOST = socket.gethostbyname(socket.gethostname())
# reserving a free port for network
PORT = 17000    
addr = (HOST, PORT)
# setting byte limit for send/receive data
header = 64
# message to handle disconnections
connect_status = "..!TERMINATED"

# Create a client socket and bind it to the address
clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clnt.connect(addr)


def send(data):
    """Send serialised data within the allotted bytes."""

    data = data.encode("utf-8")
    data_size = len(data)
    send_length = str(data_size).encode("utf-8")
    send_length += b' ' * (header - len(send_length))
    clnt.send(send_length)
    clnt.send(data)
    
    # Receive delivery message
    print(clnt.recv(1024).decode("utf-8"))

send('Hello!')
input()
send('How is it going?')
input()
send('What is the project progress?')

# Disconnect at the end of communication
send(connect_status)