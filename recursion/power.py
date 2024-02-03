def power(num,exponent):
    if exponent==0:
        return 1
    else:
        return num*power(num,(exponent-1))
    

print(power(2,3))