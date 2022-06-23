from functools import reduce

def getnopair(num):
    if num%2==1:
        return True

def add(a, b):
    return a+b

listnumbers = [1,2,3,4,5,6,7,8,9,10,11,12]

a= list(filter(getnopair, listnumbers))
print(a)

print(reduce(add, a))

