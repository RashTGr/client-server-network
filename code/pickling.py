"""Script for pickling to one of the following three 
formats: 'binary', 'JSON' and 'XML'.
"""

import pickle

import json
 
from dicttoxml import dicttoxml

import xmltodict

import pprint


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


# Serialise data in 'binary' format
def ser_bnr():
    """Create 'dat' file in static folder and write 
    data in 'binary' serialisation format.
    """
    try:
        with open('../static/serdes.dat', 'wb') as write_bnr:
            pickle.dump(tech_acronyms, write_bnr)
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    write_bnr.close()

# Deserialize 'binary' data
def des_bnr():
    try:
        with open('../static/serdes.dat', 'rb') as read_bnr:
            bnr_to_dict = pickle.load(read_bnr)
            # Pretty-print method to print dict in a well-formatted way
            pprint.pprint(bnr_to_dict)
    except EOFError:
        print("Deserialisation is completed!")
    read_bnr.close()


# Serialise data in 'json' format
def ser_json():
    """Create 'json' file in static folder and write 
    data in 'json' serialisation format.
    """
    try:
        with open('../static/serdes.json', 'w') as write_j:
            json.dump(tech_acronyms, write_j)
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    write_j.close()

# Deserialize 'json' data
def des_json():
    try:
        with open('../static/serdes.json', 'r') as read_j:
            json_to_dict = json.load(read_j)
            # Pretty print method to print dict in a well-formatted way
            pprint.pprint(json_to_dict)
    except EOFError:
        print("Deserialisation is completed!")
    read_j.close()
        

# Serialise data in 'XML' format
def ser_xml():
    """Create 'xml' file in static folder and write 
    data in 'xml' serialisation format.
    """
    try:
        with open('../static/serdes.xml', 'w') as write_xml:
            decode = dicttoxml(tech_acronyms).decode()
            write_xml.write(decode)
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    write_xml.close()

# Deserialize 'XML' data
def des_xml():
    try:
        with open('../static/serdes.xml', 'r', encoding='utf-8') as read_xml:
            my_xml = read_xml.read()
    except FileNotFoundError:
        print("Unable to open the file. Ensure file path is correct!")
    else:
        try:
            # Parse and convert it into dictionary
            xml_to_dict = xmltodict.parse(my_xml)
            # Pretty print method to print dict in a well-formatted way
            pprint.pprint(xml_to_dict)
        except EOFError:
            print("Deserialisation is completed!")
    read_xml.close()


if __name__ == "__main__":
    # Function calls
    ser_bnr()
    des_bnr()
    ser_json()
    des_json()
    ser_xml()
    des_xml()