import unittest
import socket
import pickle
import json

import client

class TestClient(unittest.TestCase):
    def setUp(self):
        # Create a mock server socket to simulate data transmission
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind(('', 0))
        self.server_sock.listen(1)

        # Connect the client socket to the mock server
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sock.connect(self.server_sock.getsockname())

    def tearDown(self):
        # Close the mock server and client sockets
        self.server_sock.close()
        self.client_sock.close()

    def test_send_binary_to_screen(self):
        # Set the appropriate flags for binary data transmission to screen
        client.binary = True
        client.to_screen = True

        # Start the client and receive mock binary data from the server
        client.send()
        self.server_sock.accept()[0].send(pickle.dumps({'test': 'data'}))

        # Assert that the client correctly receives and prints the data
        self.assertEqual(client.print.call_args[0][0], {'test': 'data'})

    def test_send_json_to_file(self):
        # Set the appropriate flags for JSON data transmission to file
        client._json = True
        client.to_file = True

        # Start the client and receive mock JSON data from the server
        client.send()
        self.server_sock.accept()[0].send(json.dumps({'test': 'data'}).encode('utf-8'))

        # Assert that the client correctly receives and writes the data to a file
        with open('received_file.txt', 'r') as f:
            self.assertEqual(f.read(), json.dumps({'test': 'data'}))
