"""Script for pickling unit test  to one of the following three 
formats: 'binary', 'JSON' and 'XML'.
"""
# Standard lib
import unittest
import pickle
import json
import pprint

# 3rd party lib
from dicttoxml import dicttoxml
import xmltodict


# Dictionary
tech_acronyms = dict(zip(['GHz', 'SSH', 'IG', 'IoT', 'M2M', 'S3', 'EC2'], 
                         ['Giga Hertz', 
                         'Secure Shell',
                         'Internet Gateway',
                         'Internet of Things', 
                         'Machine to Machine', 
                         'Simple Storage System',
                         'Elastic Compute Cloud',
                         ]))


## Assign dictionary
assign_dict = tech_acronyms


class TestSerializationFunctions(unittest.TestCase):
    def setUp(self):
        self.tech_acronyms = dict(zip(['GHz', 'SSH', 'IG', 'IoT', 'M2M', 'S3', 'EC2'], 
                         ['Giga Hertz', 
                         'Secure Shell',
                         'Internet Gateway',
                         'Internet of Things', 
                         'Machine to Machine', 
                         'Simple Storage System',
                         'Elastic Compute Cloud',
                         ]))
        self.filepath_binary = 'D:\zip file version\client-server-network-combatzone-2\static\serdes.dat'
        self.filepath_json = 'D:\zip file version\client-server-network-combatzone-2\static\serdes.json'
        self.filepath_xml = 'D:\zip file version\client-server-network-combatzone-2\static\serdes.xml'
        
    def test_ser_bnr(self):
        # Test serialization in binary format
        ser_bnr(self.tech_acronyms)
        with open(self.filepath_binary, 'rb') as f:
            data = pickle.load(f)
        self.assertEqual(data, self.tech_acronyms)
        
    def test_des_bnr(self):
        # Test deserialization in binary format
        ser_bnr(self.tech_acronyms)
        data= des_bnr(self.tech_acronyms)
        self.assertEqual(data, self.tech_acronyms)
        
    def test_ser_json(self):
        # Test serialization in JSON format
        ser_json(self.tech_acronyms)
        with open(self.filepath_json, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, self.tech_acronyms)
        
    def test_des_json(self):
        # Test deserialization in JSON format
        ser_json(self.tech_acronyms)
        data = des_json(self.tech_acronyms)
        self.assertEqual(data, self.tech_acronyms)
        
    def test_ser_xml(self):
        # Test serialization in XML format
        ser_xml(self.tech_acronyms)
        with open(self.filepath_xml, 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertEqual(data, dicttoxml(self.tech_acronyms).decode('utf-8'))
        
    def test_des_xml(self):
        # Test deserialization in XML format
        ser_xml(self.tech_acronyms)
        data = des_xml(self.tech_acronyms)
        self.assertEqual(data, self.tech_acronyms)
        

    
if __name__ == '__main__':
    unittest.main()
