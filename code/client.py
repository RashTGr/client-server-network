# Create client

import socket

Port = 17000
Server = socket.gethostbyname(socket.gethostname())
addr = (Server, Port)
header = 64
conn_status = "..!TERMINATED"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# Defining function to send info
def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(message)
    
    # Receive delivery message
    print(client.recv(2048).decode("utf-8"))

send('Hello!')
input()
send('How is it going?')
input()
send('What is the project progress?')

send(conn_status)








# # Create socket for the client
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect method for client to connect the server
# s.connect((socket.gethostname(), 1700))

# complete_info = ''
# while True:
#     msg = s.recv(7)
#     if len(msg) <= 0:
#         break
#     complete_info += msg.decode("utf-8")
# print(complete_info)