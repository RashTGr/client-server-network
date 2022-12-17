"""This is unit test for pickling script in 3 formats."""

import unittest

import pickling as pk


class PicklingTest(unittest.TestCase):
    # configure input & output to pass to each test scenario
    def setUp(self):
        self.input_all = dict(zip(['GHz', 'SSH', 'IG', 'IoT', 'M2M', 'S3', 'EC2'], 
                         ['Giga Hertz', 
                         'Secure Shell',
                         'Internet Gateway',
                         'Internet of Things', 
                         'Machine to Machine', 
                         'Simple Storage System',
                         'Elastic Compute Cloud',
                         ]))
    
        self.output_bnr = {
            'EC2': 'Elastic Compute Cloud', 
            'GHz': 'Giga Hertz', 
            'IG': 'Internet Gateway', 
            'IoT': 'Internet of Things', 
            'M2M': 'Machine to Machine', 
            'S3': 'Simple Storage System', 
            'SSH': 'Secure Shell'}
            
        self.output_js = {
            'EC2': 'Elastic Compute Cloud', 
            'GHz': 'Giga Hertz', 
            'IG': 'Internet Gateway', 
            'IoT': 'Internet of Things', 
            'M2M': 'Machine to Machine', 
            'S3': 'Simple Storage System', 
            'SSH': 'Secure Shell'}
        
        self.output_xml = {'root': {'EC2': {'#text': 'Elastic Compute Cloud', '@type': 'str'},
            'GHz': {'#text': 'Giga Hertz', '@type': 'str'},
            'IG': {'#text': 'Internet Gateway', '@type': 'str'},
            'IoT': {'#text': 'Internet of Things', '@type': 'str'},
            'M2M': {'#text': 'Machine to Machine', '@type': 'str'},
            'S3': {'#text': 'Simple Storage System', '@type': 'str'},
            'SSH': {'#text': 'Secure Shell', '@type': 'str'}}}
    
    # cleanup generated data during test cases
    def tearDown(self):
        self.input_all = 0
        self.output_bnr = 0
        self.output_js = 0
        self.output_bnr = 0

    # Unit test for each format with the given input-output data
    def test_binary(self):
        self.assertEqual(pk.ser_bnr(self.input_all), pk.des_bnr(self.output_bnr))

    def test_json(self):
        self.assertEqual(pk.ser_json(self.input_all), pk.des_json(self.output_js))

    def test_xml(self):
        self.assertEqual(pk.ser_xml(self.input_all), pk.des_xml(self.output_xml))

print("Unit tests for Serialisation is completed!")


if __name__ == "__main__":
    unittest.main()
