from socket import *
from time import sleep

ZERO = 0.025
ONE = 0.1

port = 1337

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", port))

s.listen(0)
print("Server is listening...")

c, addr = s.accept()

msg = "Some message... This is pretty neat"

covert = "a much longer secret to test if the length is not an issue" + 'EOF'
covert_bin = ""

for ch in covert:
    covert_bin += bin(ord(ch))[2:].zfill(8)

msg = msg.ljust(len(covert_bin))


print(msg)
print(covert_bin)

for i in range(len(msg)):
    c.send(msg[i].encode())
    if covert_bin[i] == "1":
        sleep(ONE)
    else:
        sleep(ZERO)

c.send("EOF".encode())
print("Message sent...")
c.close()