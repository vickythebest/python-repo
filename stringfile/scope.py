# local variables are accessible inside the function in which its defined
# local variables are accessible inside the functions inside the funciton in whihc it defined 
# local vairables are not accessible outsite of functions where its defined
# global variable are having global scope and so can be accessed anywhere
# same variables name with deff values
# convert local into global variable so you can use it outside defined function
# making change to global variable inside function

# ========================================

def myname():
    x="Vivek"
    print(x)

myname()