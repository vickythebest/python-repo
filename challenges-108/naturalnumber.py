def isNatual_Number(num):
    if num >0:
        return num*(num+1)//2
    else:
        return "No Natural Number"



input = int(input("Enter number : "))

number=isNatual_Number(input)
print(f"the sum of the first {input} natural number is : {number} ")