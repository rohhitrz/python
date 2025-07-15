a = [1, 2, 3, 4]

def double(value):
    return value*2

res=list(map(double,a));
print(res)

res2=list(map(lambda x:x**2,a));
print(res2);


#with multiple iterables

l2=[10,39,572]
l3=[20,49,772]

resNew= list(map(lambda x,y:x+y,l2,l3))
print(resNew);


#Converting to uppercase

fruits = ['apple', 'banana', 'cherry']
res=list(map(str.upper,fruits))
print(res)


#Extracting first character from strings

words=["hello","this", "is","a","list"]
res=list(map(lambda x:x[0],words));
print(res)

# something="  hello   "
# print(something.strip())

#Extracting first character from strings
s = ['  hello  ', '  world ', ' python  ']
res=list(map(lambda x:x.strip(),s));
print(res)



#Calculate fahrenheit from celsius
celsius = [0, 20, 37, 100]

f=list(map(lambda x: (x*9/5) +32 ,celsius))
print(f)





