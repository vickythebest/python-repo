def fibonacci(num):
    if num ==1:
        return num
    else:
        return num+fibonacci(num-1)
    

user=int(input("Please enter the number : "))

print(fibonacci(user))