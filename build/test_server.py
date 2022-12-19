import unittest
import socket
import pickle
import json
import xmltodict

import server

class TestServer(unittest.TestCase):
    def setUp(self):
        # Create a mock client socket to simulate data transmission
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sock.bind(('', 0))
        self.client_sock.listen(1)

        # Connect the server socket to the mock client
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.connect(self.client_sock.getsockname())

    def tearDown(self):
        # Close the mock client and server sockets
        self.client_sock.close()
        self.server_sock.close()

    def test_gr_a_server_binary_to_screen(self):
        # Set the appropriate flags for binary data transmission to screen
        server.binary = True
        server.to_screen = True

        # Start the server and send mock binary data from the client
        server.gr_a_server()
        self.client_sock.accept()[0].send(pickle.dumps({'test': 'data'}))

        # Assert that the server correctly receives and prints the data
        self.assertEqual(server.pprint.call_args[0][0], {'test': 'data'})

    def test_gr_a_server_json_to_file(self):
        # Set the appropriate flags for JSON data transmission to file
        server._json = True
        server.to_file = True

        # Start the server and send mock JSON data from the client
        server.gr_a_server()
        self.client_sock.accept()[0].send(json.dumps({'test': 'data'}).encode('utf-8'))

        # Assert that the server correctly receives and writes the data to a file
        with open('received_file.txt', 'r') as f:
            self.assertEqual(f.read(), json.dumps({'test': 'data'}))
