"""Script for pickling to one of the following three 
formats: 'binary', 'JSON' and 'XML'.
"""
# Standard lib
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

# Global variables
## File paths to save serialised data
filepath_binary = '../static/serdes.dat'
filepath_json = '../static/serdes.json'
filepath_xml = '../static/serdes.xml'

## Assign dictionary
assign_dict = tech_acronyms


# Serialise data in 'binary' format
def ser_bnr(assign_dict):
    """Create 'dat' file in static folder and write 
    data in 'binary' serialisation format.
    """    
    try:
        with open(filepath_binary, 'wb') as write_bnr:
            pickle.dump(assign_dict, write_bnr)
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    write_bnr.close()

# Deserialize 'binary' data
def des_bnr(assign_dict):
    try:
        with open(filepath_binary, 'rb') as read_bnr:
            bnr_to_dict = pickle.load(read_bnr)
            # Pretty-print method to print dict in a well-formatted way
            pprint.pprint(bnr_to_dict)
    except AttributeError:
        print("Possible data corruption or import error!")
    read_bnr.close()

# Serialise data in 'json' format
def ser_json(assign_dict):
    """Create 'json' file in static folder and write 
    data in 'json' serialisation format.
    """
    try:
        with open(filepath_json, 'w') as write_j:
            json.dump(assign_dict, write_j)
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    write_j.close()

# Deserialize 'json' data
def des_json(assign_dict):
    try:
        with open(filepath_json, 'r') as read_j:
            json_to_dict = json.load(read_j)
            # Pretty-print method to print dict in a well-formatted way
            pprint.pprint(json_to_dict)
    except EOFError:
        print("Deserialisation is completed!")
    read_j.close()
        
# Serialise data in 'XML' format
def ser_xml(assign_dict):
    """Create 'xml' file in static folder and write 
    data in 'xml' serialisation format.
    """
    try:
        with open(filepath_xml, 'w') as write_xml:
            decoded = dicttoxml(assign_dict).decode('utf-8')
            write_xml.write(decoded)
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    write_xml.close()

# Deserialize 'XML' data
def des_xml(assign_dict):
    try:
        with open(filepath_xml, 'r', encoding='utf-8') as read_xml:
            my_xml = read_xml.read()
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    else:
        try:
            # Parse and convert it into dictionary
            xml_to_dict = xmltodict.parse(my_xml)
            # Pretty-print method to print dict in a well-formatted way
            pprint.pprint(xml_to_dict)
        except EOFError:
            print("Deserialisation is completed!")
    read_xml.close()

if __name__ == "__main__":
    # Function calls
    ser_bnr(assign_dict)
    des_bnr(assign_dict)
    ser_json(assign_dict)
    des_json(assign_dict)
    ser_xml(assign_dict)
    des_xml(assign_dict)