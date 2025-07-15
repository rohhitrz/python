from functools import reduce
a = [1, 3, 5, 6, 2]

def add(x,y):
    return x+y

res=reduce(add,a)
print(res)