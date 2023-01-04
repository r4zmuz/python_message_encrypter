from cryptography.fernet import Fernet

def generate_key():
    """Generates a key for encrypting and decrypting messages."""
    return Fernet.generate_key()

def create_fernet(key):
    """Creates a Fernet instance with the given key."""
    return Fernet(key)

def encrypt(fernet, message):
    """Encrypts the given message with the given Fernet instance."""
    # Encode the message to a byte string before encrypting it
    enc_message = fernet.encrypt(message.encode())
    return enc_message

def decrypt(fernet, enc_message):
    """Decrypts the given encrypted message with the given Fernet instance."""
    # Remove the 'b' prefix from the input message
    enc_message = enc_message.lstrip("b")
    # Decrypt the message and decode the resulting byte string
    dec_message = fernet.decrypt(enc_message).decode()
    return dec_message

def main():
    """
    Welcome message and main loop of the message encryption and decryption application.
    To exit the application, press X anytime and hit enter.
    """
    print("\nWelcome to message encryption and decryption application\n"
          "To exit application press X anytime and hit enter\n")
    while True:
        print("Do you want to encrypt or decrypt the message?")
        user_input = input("Press E for encrypt or D for decrypt and hit enter: ")
        user_input = user_input.lower()
        if user_input == "d":
            try:
                enc_message = input("\nEnter message to decrypt and hit enter: ")
                dec_message = decrypt(fernet, enc_message)
                print("\ndecrypted string: ", dec_message)
                print("")
            except Exception as e:
                print("\nAn error occurred:\n", e)
        elif user_input == "e":
            message = input("\nEnter message to encrypt and hit enter: ")
            enc_message = encrypt(fernet, message)
            print("\noriginal string: ", message)
            print("encrypted message: ", enc_message)
            print("")
        elif user_input == "x":
            exit()
        else:
            print("\nEnter valid selection\n")

if __name__ == '__main__':
    # Generate a key for encryption and decryption
    key = generate_key()
    # Create a Fernet instance with the key
    fernet = create_fernet(key)
    main()
