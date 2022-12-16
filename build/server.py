# Setup the Server socket

import socket
import pickle
import json
import xmltodict
from pprint import pprint

import pickling as pk

# Parameters for configuring the 'Server' socket
## local machine name
HOST = socket.gethostbyname(socket.gethostname())
## a free port for network
PORT = 17000    
addr = (HOST, PORT)
## byte limit for send/receive data
bytesize = 5120

# Create a server socket and bind it to the address
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(addr)

# Config for data transmission
## pickling formats
binary = ''
_json = ''
xml = ''
## print to screen or to file
to_screen = ''
to_file = ''
## setting for text file
enc_txt_file = True
"""This variables serve as an actuator for calling 
a particular function.
"""

def gr_a_server():
    """Start listening for connections and pass it to 
    'connect' function for processing.
    """
    serv.listen(4)
    print(f"[LISTENING..] on host: {HOST}")
    while True:
        conn, addr = serv.accept()
        print(f"\n__DATA TRANSMISSION!__ ")
        try:
            # Binary, json, xml to 'screen'
            if binary and to_screen:
                recved = conn.recv(bytesize)
                # Pretty print method to print dict in a well-formatted way
                return pprint(pickle.loads(recved))
            elif _json and to_screen:
                recved = conn.recv(bytesize).decode('utf-8')
                # Pretty print method to print dict in a well-formatted way
                return pprint(json.loads(recved))
            elif xml and to_screen:
                recved = conn.recv(bytesize).decode('utf-8')
                # Pretty print method to print dict in a well-formatted way
                return pprint(xmltodict.parse(recved))

            # Binary, json, xml to 'file'
            elif binary and to_file:
                recved = conn.recv(bytesize)
                return pprint(pk.des_bnr(recved))
            elif _json and to_file:
                recved = conn.recv(bytesize)
                return pprint(pk.des_json(recved))
            elif xml and to_file:
                recved = conn.recv(bytesize).decode('utf-8')
                return pprint(pk.des_xml(recved))
            
            # Processing with a standalone text file
            elif enc_txt_file:
                # Create and open a NEW file to write the received data
                with open('received_file.txt', 'w') as textfile:
                    while True:
                        data = conn.recv(bytesize).decode('utf-8')
                        return textfile.write(data)
            else:
                print('The user input is required;' 
                       'please select an available configuration!')
        finally:
            print(f"\n_The Transmission is Complete!_'\n_by: [{addr}]")
            # Delivery message to clients
            conn.send("Delivered!".encode("utf-8"))
            textfile.close()
        conn.close()


if __name__ == "__main__":
    # Function call, activate listening
    gr_a_server()