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
