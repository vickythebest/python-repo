def dight_sum(number):
    digit_total =0
    if int(number) < 10:
        return number
    else:
        for i in range(len(number)):
            digit=int(number[i])
            digit_total+=digit
        return digit_total
        
number=str(input("Please enter number : "))
result=dight_sum(number)
print(result)
    