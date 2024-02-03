# computers only understands (1s & 0s) (yes or no) (true or false)
# in pyton every expression will return true or false
# if the expression is mathamatical

print(10>5) # return true as 10 is grater then 5
print(10<5) # return false as 10 is not grater then 5
print(10==5) # return false as 10 is not equal to 5
print(10==10) # return true as 10 is not equal to 10


# if the expression is not mathmatical
print("if the expression is not mathmatical")

x="vivek"
y=43
z=""
# is x true or false
# use funciton call as bool() this li evalute if is true
print("bool()")
print(bool(x)) # return true as this print true because x has some value
print(bool(y)) # return true as this print true because x has some value
print(bool(z)) # return false as this print true because x has no value


# this rule is valid for lists,tuple,dict,array etc
#  we can build a string logic based on boolean value

a=10
b=15

if (a > b):
    print("a is grater then b")
else:
    print("b is grater then a")