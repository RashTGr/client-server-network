from cryptography.fernet import Fernet

def write_key():
    """Function to generate and save a key"""
    
    # Generates a fresh fernet key
    key = Fernet.generate_key()
    with open("static/crypto.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """This function loads the saved key from the key.key directory"""

    return open("static/crypto.key", "rb").read()

# # Now generating and writing the key to a file:
#write_key()

# This key will be initialized with the Fernet class
key = load_key()

# # Converting message to bytes with 'encode' method
# message = "my secret message".encode()

# # Initializing the Fernet class with that key
# f = Fernet(key)

# # Encrypt the message
# encrypted = f.encrypt(message)

# # Decrypt the encrypted message
# decryption = f.decrypt(encrypted)

# print(decryption)



# First, writing a function to encrypt a file given the file name and key
def encrypt(filename, key):
    """Given a filename (str) and key (bytes), it encrypts the file and write it."""

    f = Fernet(key)

    # After initializing the Fernet object with the given key, let's read the target file first
    with open(filename, "rb") as file:
        """This will read all data from the file."""
        
        # File_data contains the data of the file, encrypting it
        file_data = file.read()

        # Encrypt data
        encrypted_data = f.encrypt(file_data)

        # Write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
            """Writing back the encrypted file with the same 
            name, so it will override the original.
            """

# Now, writing the decryption function
def decrypt(filename, key):
    """Given a filename (str) and key (bytes), it decrypts the 
    file and write it.
    """
    f = Fernet(key)
    with open(filename, "rb") as file:

        # Read the encrypted data
        encrypted_data = file.read()
    
    # Decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # Write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


file = "static/demo_text.txt"

# encrypt(file, key)

decrypt(file, key)


        
        