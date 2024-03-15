def insert(num):
    print("-------INSERT--------")
    num.insert(2,6)
    print(num)
    
def delete(num):
    print("-------DELETE--------")
    num.remove(4)
    print(num)

def display(num):
    print("-------DISPLAY--------")
    print(num)
    print(num[2])

def pop(num):
    print("-------TOP--------")
    t=num.pop()
    print(t)

def sort(num):
    print("-------SORT--------")
    num.sort()
    print(num)

def clear(num):
    print("-------CLEAR--------")
    num.clear()
    print(num)

def reverse(num):
    print("-------REVERSE--------")
    num.sort(reverse=True)
    print(num)

def count(num):
    print("-------COUNT--------")
    print(num.count(10))

def append(num):
    pass

l=[2,3,4]
l2=[1,5,0]
display(l)
delete(l)
insert(l)
sort(l)
pop(l)
count(l)
print("-------extend--------")
l.extend(l2)
print(l)
clear(l)
append(l)
print(5//2)
