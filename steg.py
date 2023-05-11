import sys


def bit_store(wrapper, hidden, offset, interval, sentinel):

    w_file = open(wrapper, "rb")
    w_bytearray = bytearray(w_file.read())
    wrapper = w_bytearray

    h_file = open(hiddenfile, "rb")
    h_bytearray = bytearray(h_file.read())
    hidden = h_bytearray

    # storage 
    i = 0    
    while i < len(hidden):
        
        for j in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= ((hidden[i] & 0b10000000) >> 7)

            # it is warned that this might result in values greater than 1 byte
            hidden[i] <<= 1
            offset += interval

        i += 1

    x = 0
    while x < len(sentinel):
        
        for y in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= ((sentinel[i] & 0b10000000) >> 7)

            # it is warned that this might result in values greater than 1 byte
            sentinel[i] <<= 1
            offset += interval

        i += 1
    w_file.close()
    h_file.close()
    return wrapper

# extraction
def bit_retrieve(wrapper, offset, interval, sentinel):
   
    w_file = open(wrapper, "rb")
    w_bytearray = bytearray(w_file.read())
    wrapper = w_bytearray
   
    h = bytearray()

    while (offset + 7 * interval) < len(wrapper):
        
        b = 0
        for j in range(8):
                
            b |= (wrapper[offset] & 0b00000001)
            if j < 7:

                # it is warned that this might result in values greater than 1 byte
                b <<= 1 
                offset += interval
            
        # check if b matches a sentinel byte
        # if so, we need to check further
        # if not, we can add this byte to H
        # but we may need to add matched partial sentinel bytes first!
        # afterwards...
        
        if (b == sentinel[0]):
            sentinel_check = offset + interval
            is_sentinel = True
            
            for i in range(5):
                if ((sentinel_check + 7*interval) < len(wrapper)):
                    testByte = 0
                    for j in range(8):
                        testByte |= (wrapper[sentinel_check] & 0b00000001)
                        if (j < 7):
                            testByte <<= 1
                            sentinel_check += interval
                    
                    if (testByte != sentinel[i+1]):
                        is_sentinel = False
                        break
                
                    else:
                        break
                testByte += interval
            
            if(is_sentinel):
                return h
        
        h.append(b)
        offset += interval
    
    w_file.close()
    return h
    

def byte_store(wrapper, hidden, offset, interval, sentinel):

    w_file = open(wrapper, "rb")
    w_bytearray = bytearray(w_file.read())
    wrapper = w_bytearray

    h_file = open(hiddenfile, "rb")
    h_bytearray = bytearray(h_file.read())
    hidden = h_bytearray

    i = 0
    while i < len(hidden):
        wrapper[i] = hidden[i]
        offset += interval
        i += 1

    i = 0
    while i < len(sentinel):
        wrapper[offset] = sentinel[i]
        offset += interval
        i += 1

    w_file.close()
    h_file.close()
    return wrapper

# storage
def byte_retrieve(wrapper, offset, interval, sentinel):
    
    w_file = open(wrapper, "rb")
    w_bytearray = bytearray(w_file.read())
    wrapper = w_bytearray   
   
    h = bytearray()

    while offset < len(wrapper):
        b = wrapper[offset]

        # check if b matches a sentinel byte
        # if so, we need to check further
        # if not, we can add this byte to H
        # but we may need to add matched partial sentinel bytes first!
        #afterwards...

        if b == sentinel[0]:
            sentinel_track = offset + interval
            is_sentinel = True
            
            for i in range(5):
                if (sentinel_track < len(wrapper)):
                    testByte = wrapper[sentinel_track]
                else:
                    is_sentinel = False
                    break
                
                if (testByte != sentinel[i+1]):
                    is_sentinel = False
                    break
                sentinel_track += interval
            
            if(is_sentinel):
                return h

        h.append(b)
        offset += interval

    w_file.close()
    return h


if __name__ == "__main__":
    
    if(len(sys.argv) < 4 or len(sys.argv) > 7):
        print("Invalid input. Run in command line with python steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")        

    # given sentinel bytes from the pdf
    sentinel = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

    offset = 0
    interval = 1

    # take the user input assign to variables
    mode = str(sys.argv[1])
    bitmode = str(sys.argv[2])
    wrapperfile = ""
    hiddenfile = ""

    print((sys.argv[3])[2:])

    for i in range(len(sys.argv)):
        if(((sys.argv[i])[0:2]) == '-o'):
            offset = (sys.argv[i])[2:]
        if(((sys.argv[i])[0:2]) == '-i'):
            interval = (sys.argv[i])[2:]
        if(((sys.argv[i])[0:2]) == '-w'):
            wrapperfile = (sys.argv[i])[2:]
        if(((sys.argv[i])[0:2]) == '-h'):
            hiddenfile = (sys.argv[i])[2:]

    offset = int(offset)
    interval = int(interval)
        
    if(bitmode == "-b" and mode == "-s"):
        final = bit_store(wrapperfile, hiddenfile, offset, interval, sentinel)
    elif(bitmode == "-b" and mode == "-r"):
            final = bit_retrieve(wrapperfile, offset, interval, sentinel)
    elif(bitmode == "-B" and mode == '-s'):
        final = byte_store(wrapperfile, hiddenfile, offset, interval, sentinel)
    elif(bitmode == "-B" and mode == '-r'):
        final = byte_retrieve(wrapperfile, offset, interval, sentinel)
    sys.stdout.buffer.write(final)

