# swapping two variables
# a,b=5,10
# print(a,b)
# b,a=a,b
# print(a,b)

#count characters of string

# word="python"
# print(len(word));

#global and local variables


# msg="hi I am Global"

# def func():
#     msg="Hi I am Local"
#     print(msg)

# func()
# print(msg);


# def fun():
#     s += 'GFG'  
#     print("Inside Function", s)

# s = "I love Geeksforgeeks"
# fun()


def fun():
    global s
    s += 'GFG'  
    print("Inside Function", s)

s = "I love Geeksforgeeks"
fun()