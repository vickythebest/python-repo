def calculate_power(base,exponent):
    result=1
    for _ in range(int(exponent)):
        result *= base
    return result
    # return base ** exponent


base=int(input("Enter the base number : "))
exponent=int(input("Enter the base number : "))


result=calculate_power(base,exponent)
print(f"The power of {base} is {result}")