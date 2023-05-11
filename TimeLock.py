import sys
from datetime import datetime
import hashlib
###################################################################
# Run in command line with 'python TimeLock.py YYYY MM DD HH mm SS'
###################################################################

# Returns true if time is within daylight savings time, false otherwise.
def is_DST(dt):
    if(dt.month in [4,5,6,7,8,9,10]):
        return True
    elif((dt.month == 3 and dt.day > 12) or (dt.month == 3 and dt.day == 12 and dt.hour >= 6)):
        return True
    elif((dt.month == 11 and dt.day < 5) or (dt.month == 11 and dt.day == 5 and dt.hour < 6)):
        return True
    
    return False


def calculate(year, month, day, hour,minute, second):
    current_time = datetime.now()
    epoch = datetime(year, month, day, hour, minute, second)

    # finds difference in seconds between epoch and current time
    diff = (current_time-epoch)
    time_diff = 0
    time_diff += (diff.days * 86400)
    time_diff += (diff.seconds)
    
    # adds/subtracts an hour if needed according to daylight savings time
    if(is_DST(current_time) and not is_DST(epoch)):
        time_diff -= 3600
    elif(is_DST(epoch) and not is_DST(current_time)):
        time_diff += 3600 

    # sets minute_interval to the beginning of the minute of the difference between the current time and the epoch time.
    minute_interval = time_diff - (time_diff % 60)
    minute_interval = str(minute_interval)

    # hash the time difference twice using md5
    first_hash = hashlib.md5(minute_interval.encode())
    first_md5 = first_hash.hexdigest()
    first_md5 = str(first_md5)
    
    second_hash = hashlib.md5(first_md5.encode())
    second_md5 = second_hash.hexdigest()

    hash = str(second_md5)

    # returns a string of the first 2 letters left to right and the first 2 numbers right to left of the hash.
    final_str = ""
    for i in range(len(hash)):
        if((len(final_str) < 2) and hash[i] in ['a', 'b', 'c', 'd', 'e', 'f']):
            final_str += hash[i]
    for i in range(len(hash)-1, 0, -1):
        if((len(final_str) < 4) and hash[i] in ['0', '1', '2', '3', '4', '5', '6', '7' , '8', '9']):
            final_str += hash[i]
    
    return final_str


if(len(sys.argv) != 7):
    print("Incorrect input. Please give YYYY MM DD HH mm SS as arguments.")
    exit()
    
# exucutes calculate function using the command line arguments as the epoch
code = calculate(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]))
print(code)