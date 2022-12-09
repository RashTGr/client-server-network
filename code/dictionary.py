# Creating a dictionary

import pickle

tech_acronyms = dict(zip(['CPU', 'IoT', 'GHz', 'CLI', 'FTP', 'LAN', 'WAN'], 
                         ['Central Processing Unit', 
                         'Internet of Things', 
                         'Central Processing Unit', 
                         'Giga Hertz', 
                         'File Transfer Protocol', 
                         'Local Area Network', 
                         'Wide Area Network',
                         ]))

serialise = pickle.dumps(tech_acronyms)

print(serialise)