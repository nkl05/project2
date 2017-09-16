from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    sender = select_friend()

    secret_image = raw_input("Enter the name of encrypted image here : ")
    secret_image = Steganography.decode(secret_image)

    print "your friend has sent you this message :" + secret_image
