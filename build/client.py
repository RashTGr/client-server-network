# Setup the Client socket

import os
import socket
import pickle
import json
from dicttoxml import dicttoxml

import pickling as pk


# Parameters for configuring the 'Client' socket
## getting local machine name
HOST = socket.gethostbyname(socket.gethostname())
## reserving a free port for network
PORT = 17000    
addr = (HOST, PORT)
## setting byte limit for send/receive data
bytesize = 5120


# Create a client socket and bind it to the address
clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clnt.connect(addr)

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
## Text file parameters
filepath = "../static/demo_text.txt"
filesize = os.path.getsize(filepath)
"""This variables serve as an actuator for calling 
a particular function.
"""

# Data to be passed to the server
tech_dict = pk.tech_acronyms


def send():
    """Send serialised data within the allotted bytes."""
    # Send dictionary with pickling formats
    while True:
        try:
            # Binary, json, xml to 'screen' 
            if binary and to_screen:
                serialised = pickle.dumps(tech_dict)
                return clnt.send(serialised)

            elif _json and to_screen:
                serialised = json.dumps(tech_dict)
                return clnt.send(serialised.encode('utf-8'))

            elif xml and to_screen:
                serialised = dicttoxml(tech_dict)
                return clnt.send(serialised)

            # Binary, json, xml to 'file'
            elif binary and to_file:
                serialised = pk.ser_bnr(tech_dict)
                try:
                    return clnt.send(str(serialised).encode('utf-8'))
                except (AttributeError, TypeError):
                    print('NonType object encoding issue. Please check the source code!')
            elif _json and to_file:
                serialised = pk.ser_json(tech_dict)
                try:
                    return clnt.send(str(serialised).encode('utf-8'))
                except (AttributeError, TypeError):
                    print('NonType object encoding issue. Please check the source code!')
            elif xml and to_file:
                serialised = pk.ser_xml(tech_dict)
                try:
                    return clnt.send(str(serialised).encode('utf-8'))
                except (AttributeError):
                    print('NonType object encoding issue. Please check the source code!')
            
            # Processing with a standalone text file
            elif enc_txt_file:
                # Open the file to read and send data
                with open(filepath, 'r') as textfile:
                    while True:
                        data = textfile.read()
                        if not data:
                            break
                        return clnt.send(data.encode('utf-8'))
            else:
                print('The user input is required;' 
                       'please select an available configuration!')    
        finally:
            # Delivery message from server
            print(clnt.recv(bytesize).decode("utf-8"))
            textfile.close()
        clnt.close()              


if __name__ == "__main__":
    # Function call    
    send()