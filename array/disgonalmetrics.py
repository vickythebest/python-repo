def digonalMetrics(arr):
    num=[int(digit) for digit in str(arr)]
    
    n=len(num)
    result=[[0]*n for _ in range(n)]

    for i in range(n):
        result[i][i]=num[i]
    
    for i in result:
        print(i)    
    
# num=[1,2,3,4,5]
num=12345
digonalMetrics(num)