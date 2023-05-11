import os
import sys
import base64

# SETTINGS
KEY_FILE = "key2"




# main
if __name__ == '__main__':
    # method for xor'ing two file together
    key = bytearray(open(KEY_FILE, "rb").read())
    cipher = bytearray(sys.stdin.buffer.read())
    sys.stdout.buffer.write(bytearray(a ^ b for a, b in zip(cipher, key)))
