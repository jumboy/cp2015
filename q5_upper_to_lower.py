__author__ = 'jinya_000'

import binascii
letter = input("Enter an upper case letter: ")
if letter == letter.lower():
    print("error")
else:
    print("The lower case letter is: " + chr(ord(letter)+32))