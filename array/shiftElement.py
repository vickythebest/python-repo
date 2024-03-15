# Shift 2 element from left to rigth fill the 0 at empty index
def shiftElements(num,index):

    i=0
    while index < len(num):
        num[i]=num[index]
        index=index+1
        i=i+1
    
    while i < len(num):
        num[i]=None
        i=i+1


    print(num)

num =[1,2,3,4,5,4,3,2,1]
shiftElements(num,4)