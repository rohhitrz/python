# # print(type(type(int)))

# # li = ['a','b','c','d']
# # print("".join(li))

# print(ord("A"))
# print(chr(65))


# import re
# s = 'horses are fast'

# regex = re.compile(r'(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
# matched = re.search(regex, s)

# if matched:
#     print(matched.groupdict())


# li= [3, 4, 5, 20, 5, 25, 1, 3]
# print(li.pop(1))
# print(li)

# import time


# print(time.time())


def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

closure = outer()
print(closure())
print(closure())