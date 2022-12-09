# Create client

import socket

Port = 17000
Server = socket.gethostbyname(socket.gethostname())
addr = (Server, Port)
header = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# # Defining function to send info
# def send(msg):
#     message = msg.encode("utf-8")
#     msg_length = len(message)
#     send_length = str(msg_length).encode("utf-8")
#     send_length += b' ' * (header - len(send_length))
#     client.send(send_length)
#     client.send(message)

# send('Hello!')









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