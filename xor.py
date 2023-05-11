import os
import sys
import base64

# main
if __name__ == '__main__':
    if(len(sys.argv) == 3):
        KEY_FILE = sys.argv[1].replace(".py","")
        CIPHER_FILE = sys.argv[2].replace(".py","")
        # method for xor'ing two file together
        key = bytearray(open(KEY_FILE, "rb").read())
        cipher = bytearray(open(CIPHER_FILE, "rb").read())
        sys.stdout.buffer.write(bytearray(a ^ b for a, b in zip(cipher, key)))
    else:
        print("Incorrect usage.\n$ python xor.py <key> <cipher>")