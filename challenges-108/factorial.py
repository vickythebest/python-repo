print("Calculate the factorial")
number=int(input("Enter the number : "))
print("Calculate the factorial of ",number)

def factorial(number):
    fact=1
    while number >= 1:
        fact *=number
        number = number-1
    return fact

print(factorial(number))
