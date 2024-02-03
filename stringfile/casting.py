x="1" #string
y=55 #int
z=27.01 #float

print(type(x))
print(type(y))
print(type(z))

print("we need python to consider as different/custom datatype (i.e int as float)")

print("define integer to float / string nby using construct function")

y=float(55)

print(type(y))

print("convert float to integer")
z=int(27.01)
print(type(z)," : ",z)

print("convert float to string")
z=str(27.01)
print(type(z), ":", z )

print("convert complext")

z=complex(27.01)
print(type(z)," : ",z)

# you cann't change from coplex to other dattype
#  you can't chagne text to datatype 

name="vivek"
print(type(name),name)

name=int(name) #error invalid literal for int() with base 10: 'vivek'