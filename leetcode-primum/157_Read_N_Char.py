

def read(self,buf,n):
    bufindex=0
    tempbuf=''*4

    while bufindex < n:
        char4read=read4(tempbuf)

        if char4read == 0:
            break
        
        minchar=min(char4read,n-bufindex)

        for i in range(len(minchar)):
            buf[bufindex]=tempbuf[i]
            bufindex+=1
    return bufindex
