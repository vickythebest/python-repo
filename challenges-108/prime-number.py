number=int(input("Enter the number : "))

if number >1:
        
    for i in range(2,number):
        
        if (number%i)==0:
            print("Not a prime number")
            break
    else:
        print(number, "is prime number")
else:
    print(number, "is prime number")