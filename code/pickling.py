
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
    with open('../static/serdes.dat', 'wb') as write_bnr:
        """Create 'dat' file in static folder and write 
        data in 'binary' serialisation format.
        """
        pickle.dump(tech_acronyms, write_bnr)
    write_bnr.close()

# Deserialize 'binary' data
def des_bnr():
    with open('../static/serdes.dat', 'rb') as read_bnr:
            reached_to_end = False
            while not reached_to_end:
                try: 
                    pprint.pprint(pickle.load(read_bnr))
                except EOFError:
                    reached_to_end = True
            read_bnr.close()


# Serialise data in 'json' format
def ser_json():
    with open('../static/serdes.json', 'w') as write_j:
        """Create 'json' file in static folder and write 
        data in 'json' serialisation format.
        """
        json.dump(tech_acronyms, write_j)
    write_j.close()

# Deserialize 'json' data
def des_json():
    with open('../static/serdes.json', 'r') as read_j:
        # Pretty print method to print dict in a well-formatted way
        pprint.pprint(json.load(read_j))
    read_j.close()
        

# Serialise data in 'XML' format
def ser_xml():
    with open('../static/serdes.xml', 'w') as write_xml:
        """Create 'xml' file in static folder and write 
        data in 'xml' serialisation format.
        """
        decode = dicttoxml(tech_acronyms).decode()
        write_xml.write(decode)
    write_xml.close()

# Deserialize 'XML' data
def des_xml():
    with open('../static/serdes.xml', 'r', encoding='utf-8') as read_xml:
        my_xml = read_xml.read()
    # Parse and convert it into dictionary
    xml_to_dict = xmltodict.parse(my_xml)
    # Pretty print method to print dict in a well-formatted way
    pprint.pprint(xml_to_dict)



if __name__ == "__main__":
    # Function calls
    ser_bnr()
    des_bnr()
    # ser_json()
    # des_json()
    # ser_xml()
    # des_xml()