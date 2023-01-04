from cryptography.fernet import Fernet

# generate a key for encryption and decryption

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)

def encrypt():
    # get user input
    message = input("Enter message to encrypt and hit enter: ")

    # then use the Fernet class instance
    # to encrypt the string, string must
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
    print("")
    print("original string: ", message)
    print("encrypted message: ", encMessage)
    print("")


def decrypt():
    #get decryption input
    message2 = input("Enter message without prefix 'b' to decrypt and hit enter: ")

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods
    decMessage = fernet.decrypt(message2).decode()

    print("decrypted string: ", decMessage)
    print("")



if __name__ == '__main__':

    print("\nWelcome to message encryption and decryption application\n"
          "\nTo exit application press X anytime and hit enter\n")
    while True:
        print("Do you want to encrypt or decrypt the message?")
        userInput2 = input("Press E for encrypt or D for decrypt and hit enter: ")
        userInput2.lower()
        if userInput2 == "d":
            print("")
            decrypt()
        elif userInput2 == "e":
            print("")
            encrypt()
        elif userInput2 == "x":
            exit()
        else:
            print("\nEnter valid selection\n")

