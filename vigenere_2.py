# Imported needed libraries
import sys

# Set better names for variables
mode = sys.argv[1]
key = sys.argv[2]
# Booleans for stdio
stdin = sys.stdin.isatty
stdout = sys.stdout.isatty
# define encoding type
sys.stdin.reconfigure(encoding='utf-8')

### DEFINE FUNCTIONS ###
# Vigenere encryption function
def envigenere(text,key):
    # Set output string and an offset used to maintain key position after skipping special characters
    textout = ""
    offset = 0
    # Iterate through each character
    for i in range(len(text)):
        # Get characters at index i
        tchar = text[i]
        kchar = key[i-offset]
        if (tchar.isalpha()): # If the text's character is an alpha letter
            # Translate the text character and key character to a range of 0-25
            tunicode, tupper = shift(tchar)
            kunicode, kupper = shift(kchar) #kupper isnt actually used. Just a byproduct from the shift() function since shift() is reused to support both the text and the key
            # Add the values and mod 25 (rotation)
            outunicode = (tunicode+kunicode)%26
            # Append character to output string
            textout += unshift(outunicode,tupper)
        else: # Text's character is a special character (not alpha)
            # Increment offset and append character to output string
            offset += 1
            textout += tchar
    return textout

# Vigenere decryption function
def devigenere(text, key):
    # Set output string and an offset used to maintain key position after skipping special characters
    textout = ""
    offset = 0
    # Iterate through each character
    for i in range(len(text)):
        # Get characters at index i
        tchar = text[i]
        kchar = key[i-offset]
        if(tchar.isalpha()): # If the text's character is an alpha letter
            # Translate the text character and key character to a range of 0-25
            tunicode, tupper = shift(tchar)
            kunicode, kupper = shift(kchar) #kupper isnt actually used. Just a byproduct from the shift() function since shift() is reused to support both the text and the key
            # Subtract the values and mod 25 (rotation)
            outunicode = (tunicode-kunicode)%26
            # Append character to output string
            textout += unshift(outunicode, tupper)
        else: # Text's character is a special character (not alpha)
            # Increment offset and append character to output string
            offset += 1
            textout += tchar
    return textout



# Function to "fix" the key to be used by the encryption and decryption function
def fixkey(key, textlen):
    # Delete spaces
    key = key.replace(" ", "")
    # If key is shorter than text, repeat it appropriately and return it
    if (len(key) < textlen): return (key*(int(textlen/len(key)+1)))[:textlen]
    # Key is longer than text and is fine, return it
    return key

# Function to translate characters to a range of 0-25
def shift(char):
    if (char.isupper()):
        upper = True
        offset = 65
    else:
        upper = False
        offset = 97
    return (ord(char)-offset), upper

# Function to undo shift. Translates numbers to their original range (keeping case)
def unshift(num, upper):
    if upper:
        return chr(num+65)
    else:
        return chr(num+97)


### MAIN ***
# Check if called with enough args and contains compatible modes
if (len(sys.argv)<=2) or (not (sys.argv[1] == "-e" or sys.argv[1] == "-d")):
    # Incorrect call and help info
    print("Incorrect usage.\n\n$ python vigenere.py <mode> <key>\n\n\
<mode>\n\t-e : encrypt a message using the given key\n\
\t-d : decrypt a message using the given key\n\
<key>\n\tA string used to encrypt or decrypt the message.")

else:
    # Main loop
    while(True):
        if (stdin): # Redirect input if stdin is present
            textin = sys.stdin.read()
        else: # If not, regular input
            textin = input()

        # "Fix" the key
        key = fixkey(key,len(textin))

        if (mode == "-e"): # Encrypting
            textout = envigenere(textin,key)

        elif (mode == "-d"): # Decrypting
            textout = devigenere(textin,key)

        # Print output. (stdout will be routed to file)
        print(textout)

        break #needs to change when input works correctly to not break in that case
    



