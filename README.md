# TCP Client-Server Network application

## Description
This is a simple server-client network application with features for sending and receiving data between endpoints, written in Python's socket module. The socket type is socket.SOCK_STREAM and TCP is a default protocol. The round-trip section, which is in the middle, is where data is transferred between the client and server through calls to `.send()` and `.recv()`.
Although built on a local machine, this application can also be configured for different machines interconnected via a local network or an external network.

## Features
The following features are configured for transmitting data in this particular application:
- Send and receive dictionary in three pickling formats: binary, JSON and XML.
- The ability to handle encrypted contents.
- Send and receive text files.
- Encrypt and decrypt text files.
- A configurable option to print the contents of sent items to the screen or to a file.

In this project, the **`unittest`** module is used to check the core features of the application.


## Installation
This project was written in Python language, and its functions can be run using a terminal or any Python-compatible interpreter. Please ensure that ***Pipfile*** is used when installing this application. 
The ***Pipfile*** incorporated into the new tool `pipenv` as a handy replacement for the conventional **dependencies<sup>(requirements)</sup>** file and contains necessary dependencies. If a virtual environment doesn't exist, `pipenv` creates one to store the package and you can manage runtime dependencies separately from development dependencies, which are tracked and locked. To effectively use `pipenv`, you don't have to disassemble your project and start over from scratch; instead, you can migrate from existing traditional requirements.txt files: 
```bash
pipenv install -r requirements.txt
```

Alternatively, with the following command you can create the **requirements** file based on the existing **Pipfile**:
```bash
$ pipenv lock -r > requirements.txt  
$ pipenv lock -r -d > dev-requirements.txt
```
If you wish to learn more about `pipenv`, please follow the source from [Basic Usage of Pipenv](https://docs.pipenv.org/).


## Usage
Prior to running the **`client.py`** script to begin data transmission, the **`server.py`** script must first be run to ensure it is in listening mode. Please look at lines 25 to 37 in both scripts if you want to change the configuration. You may pick any of the following combinations as long as the same combinations are used for both server and client files, and before executing the changes, make sure the files are saved:
- Binary to screen
- JSON to screen
- XML to screen
- Binary to a file
- JSON to a file
- XML to a file
- Transfer encrypted text file

Some commands to get started are provided below, assuming the user is in the right path -> **..\Client-Server\build>**:

##### Step 1. Start SERVER [terminal_01]
```bash
$ server.py
```

##### Step 3. Start CLIENT [terminal_02]
```bash
$ client.py
```

```Python
# Pickling in three formats: binary, JSON and XML
pickling.py

# Encryption and Decryption
encrypt_fn.py

# Run any of the tests
test_server.py
```


## Contribution 
If you have any suggestions for how we can better improve this project, we'd love to hear them.


## Contributors
- `Rashad Gurbanli`
- `Seba Qasim`
- `Lee Ho Yan`
