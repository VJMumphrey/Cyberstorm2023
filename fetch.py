from ftplib import FTP

# FTP server details
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
USE_PASSIVE = True # set to False if the connection times out
METHOD = 10 # 7 or 10
FOLDER = str(METHOD) + "/"

# connect and login to the FTP server
ftp = FTP()
print("connecting")
ftp.connect(IP, PORT)
print("connected")
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

words = ""
# if method is 7, get the rightmost 7 bits of each
if METHOD == 7:
    # iterate through each file permission
    for f in files:
        # store permissions
        b = f[3:10]
        fakeBits = f[0:3]
        res = ""
        # iterate through permissions and turn it into binary
        # check if dummy file
        fake = False
        for c in fakeBits:
            if(c != '-'):
                fake = True
                break
        # if the file isnt a dummy, change it from binary to ascii
        if(not fake):
            for p in range(len(b)):
                if b[p] == "-":
                    res += '0'
                else:
                    res += '1'

        # binary to ascii and append to words string
            words += chr(int(res,2))

elif METHOD == 10:
    bytes = []
    binaryString = ""
    for f in files:
        b = f[0:10]
        res = ""
        # 0 for -, 1 for anything but -
        for p in range(len(b)):
            if(b[p] == '-'):
                res += '0'
            else:
                res += '1'
        # save binary in a string
        binaryString += res

    # seperate binary string into 7 bit binary
    for i in range(0,len(binaryString), 7):
        bytes.append(binaryString[i:i+7])

    # turn binary to ascii
    for j in range(len(bytes)):
        words += chr(int(bytes[j],2))

# output
print(words)
