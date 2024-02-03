# Single line string
name="vivek"
# Multiline String
x="""this is a random string 
this is the 
second line of the string"""

print(x)


# indexing & negative indexing
name="vivek"

# VISULIZATION STRING
#  v  i  v  e  k
#  0  1  2  3  4 # indexing
# -5 -4 -3 -2 -1 # negative indexing

print(name[3]) # this print 3 char of string
print(name[-5])# this pring -5 char of stirng 

print(name[2:])# this print char from index 2 to end
print(name[:2])# this print char before index 2

print(name[1:4])# Included: excluded this is the syntec

print(name.upper())

name=name.upper()
print(name)

lowername=name.lower()
print(lowername)

fname="vivek"
lname="kumar"

# remove white space
fname=fname.strip()

print(fname+" "+lname)
print(fname,lname)

# Replace char in string
item="chair"

print(item.replace("c","k"))


# SPLIT
message="Hi, this ids vivek, i'm developer"
print(message.split(","))

# Formatting
name="vivek"
age =43
# my name is rakesh and my age is 43
introduction="my name is {} and age is {}"

print(introduction.format(name,age))

