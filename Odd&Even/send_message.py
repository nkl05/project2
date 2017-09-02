from datetime import datetime
from select_friend import select_friend
from steganography.steganography import Steganography
import re

def send_message():
    friend_choice = select_friend()

    original_image = raw_input("Enter the name of the image to hide the message : ")
    pattern = '^[0-9a-zA-Z\s]+\.jpg$'
    if(re.match(pattern,original_image) !=None):
        output_image = raw_input("enter name of the output image : ")
        text = raw_input("enter your secret message : ")

        #now the encryption of message is running
        Steganography.encode(original_image,output_image,text)
        new_chat = {
            "message" : text,
            "Date & Time" :datetime.now()
        }