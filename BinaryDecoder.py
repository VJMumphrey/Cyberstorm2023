#import sys module for stdin
import sys

# Reads binary message from stdin
text = sys.argv[1]

# Converts the binary to a list of 7- or 8- bit chunks
bytes = []

# finds if input is 7- or 8- bit ASCII
if((len(text)%7==0) and len(text)%8!=0):
        for i in range(0,len(text), 7):
                bytes.append(text[i:i+7])

else:
        for i in range(0,len(text), 8):
                bytes.append(text[i:i+8])

# Converts each 7- or 8-bit chunk into the corresponding ASCII character
str = ""
for i in range(len(bytes)):
        str += chr(int(bytes[i], 2))

# Print the decoded text
print(str)