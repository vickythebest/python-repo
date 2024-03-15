def intersection(num1,num2):
    result=[]

    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i]==num2[j]:
                result.append(num1[i])
    
    print(result)

def intersection2(num1,num2):
    result=set()
    num2=set(num2)
    for i in num1:
        if i in num2:
            result.add(i)

    print(result)

a=[1,2,3]
b=[2,3,4]
intersection(a,b)
a=[11,12,13]
b=[12,13,14]
intersection2(a,b)