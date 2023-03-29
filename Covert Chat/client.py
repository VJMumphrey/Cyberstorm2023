from socket import *
from sys import stdout
from time import time

ZERO = 0.025
ONE = 0.1
threshhold = (ZERO + ONE)/2


iplist = ["localhost","138.47.99.64"]
ip = iplist[0]
port = 31337

# AF_INET is a network stack
# Type of communication (TCP protocol)
s = socket(AF_INET, SOCK_STREAM)

s.connect((ip, port))

data = s.recv(4096).decode()

msg = ""
covert_bin = ""

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    msg += data
    stdout.flush()
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3)
    stdout.write(f" {delta}\n")
    if delta < threshhold:
        covert_bin += "0"
    else:
        covert_bin += "1"

covert = ""
for i in range (0,len(covert_bin), 8):
    covert += chr(int(covert_bin[i:i+8], 2))

s.close()
covert = covert[:len(covert)-3]
stdout.write(msg)
stdout.write(covert)