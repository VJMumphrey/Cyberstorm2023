from socket import *
from sys import stdout
from time import time

ZERO = 0.1
ONE = 0.025
threshhold = (ZERO + ONE)/2


iplist = ["localhost","138.47.99.64"]
ip = iplist[1]
port = 31337

# AF_INET is a network stack
# SOCK_STREAM is the type of communication (TCP protocol)
s = socket(AF_INET, SOCK_STREAM)

print("[connect to the chat server]")
s.connect((ip, port))

data = s.recv(4096).decode()

msg = ""
covert_bin = ""

print("...")
while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    msg += data
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3)
    if delta < threshhold:
        covert_bin += "0"
    else:
        covert_bin += "1"

stdout.write("...\n")

print("[disconnect from the chat server]")
s.close()

covert = ""
for i in range (0,len(covert_bin), 8):
    covert += chr(int(covert_bin[i:i+8], 2))

covert = covert[:len(covert)-3]
stdout.write(f"Covert message: {covert}\n")
stdout.flush()

