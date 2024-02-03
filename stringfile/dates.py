# module for date
import datetime
# check dir inside datetime
# print(dir(datetime))
# print(dir(datetime.datetime))


# print current date
print(datetime.datetime.now())


# print current day
mytimevariable=datetime.datetime.now()
print(mytimevariable.day)
print(mytimevariable.year)
print(mytimevariable.strftime("%A"))
print(mytimevariable.strftime("%B"))
print(mytimevariable.strftime("%C"))
print(mytimevariable.strftime("%D"))
print(mytimevariable.strftime("%T"))
print(mytimevariable.strftime("%H"))

# print current month
# creating a date
mycustdate=datetime.datetime(1980,3,1)
print(mycustdate.strftime("%D"))

# userinput=input("Enter date ")
# print("you enterent ", userinput)
# guess day/month of a given date
# list of strftime ref


