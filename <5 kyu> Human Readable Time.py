'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
'''



def make_readable(seconds):
    ntime = []
    if seconds < 60:
        time=["00","00", seconds]
        
    elif seconds < 3600:             #minutes
        minu = seconds // 60
        sec = seconds % 60
        time=["00",minu, sec]
        
    else:                            #hour
        hour = seconds // 60//60
        minu = (seconds // 60)% 60
        sec = seconds % 60 
        time = [hour, minu, sec]
    for x in time:
        if len(str(x))==1:
            ntime.append('0'+str(x))
        else:
            ntime.append(str(x))
    return "{}:{}:{}".format(ntime[0],ntime[1],ntime[2])
