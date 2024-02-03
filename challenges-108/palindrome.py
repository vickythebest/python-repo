def isPalindrome(number):
    left=0
    right=len(number)-1
    if int(number) <10:
        return True
    else:
        while left < right:
            if number[left]!=number[right]:
                return False
            else:
                left+=1
                right-=1
        return True



user=input("Enter number : ")
print(isPalindrome(user))