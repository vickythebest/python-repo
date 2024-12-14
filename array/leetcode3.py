def substring(num):
    count=1
    size=1
    i=0
    j=0
    temp=set()
    while(j<len(num)-1):
        if num[j] not in temp:
            temp.add(num[j])
            count=(j-i+1)
            j=j+1
        else:
            while num[i] in temp:
                temp.remove(num[i])
                i=i+1
            j=j+1
    print('size',count)
        
        



num='bbbb'
# num='pwwkew'
# num='abcabcbb'
substring(num)