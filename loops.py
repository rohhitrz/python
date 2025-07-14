# s = ["hello", "ok", "no hello"]

# for i in s:
#     print(i);


# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)


# a = ["shirt", "sock", "pants", "sock", "towel"]

# for i in a:
#     if i == "pants":
#         continue
#     print(i)

# *agrs **kwargs


# *agrs

# def func(*argv):
#   for arg in argv:
#     print(arg)

# func("name","shame","came");


# #  **kwargs
# def function(**kwargs):
#   for k,v in kwargs.items():
#     print("%s==%s" % (k,v))

# function(name="Rohit", age=24);

#anonymous function

# func_cube=lambda x:x**3

# print(func_cube(4))


#recursive function

def factorial(n):
    if(n==0):
        return 1
    
    else:
        return n * factorial(n - 1) 



print(factorial(5));