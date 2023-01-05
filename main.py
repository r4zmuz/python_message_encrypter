import sys
from idlelib import window
from turtle import window_width, window_height

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
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
    return enc_message.decode()

def decrypt(fernet, enc_message):
    """Decrypts the given encrypted message with the given Fernet instance."""
    # Remove the 'b' prefix from the input message
    enc_message = enc_message.lstrip("b")
    # Decrypt the message and decode the resulting byte string
    dec_message = fernet.decrypt(enc_message).decode()
    return dec_message

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # Create the widgets
        self.setGeometry(100, 100, 600, 100) #set window size
        self.label = QLabel("Enter message:", self)
        self.line_edit = QLineEdit(self)
        self.encrypt_button = QPushButton("Encrypt", self)
        self.decrypt_button = QPushButton("Decrypt", self)
        self.enc_label = QLabel("", self)  # create an instance of QLabel

        # Set up the layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.enc_label)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)
        self.setLayout(layout)

        # Connect the buttons to the slots
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

    def encrypt(self):
        message = self.line_edit.text()
        enc_message = encrypt(fernet, message)
        self.label.setText("Encrypted message:")
        self.enc_label.setText(enc_message)


    def decrypt(self):
        enc_message = self.line_edit.text()
        dec_message = decrypt(fernet, enc_message)
        self.label.setText("Decrypted message:")
        self.enc_label.setText(dec_message)

if __name__ == '__main__':
    # Generate a key for encryption and decryption
    key = generate_key()
    # # Create a Fernet instance with the key
    fernet = create_fernet(key)
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Create an instance of MainWindow
    window = MainWindow()
    #set window size
    # Show the window
    window.show()
    # Run the application's event loop
    sys.exit(app.exec_())

