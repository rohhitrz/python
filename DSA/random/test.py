# #lets try to count digits

# def count(num):
#      num = abs(num)
#      count=0
#      if num == 0:
#         return 1 
#      while(num>0):
#           num=num//10
#           count=count+1
   
#      return count


# print(count(34231))



# #approach2
# def count2(num):
#     return len(str(abs(num)))

# print(count2(12345678910))

# #approach3
# def count2(num):
#     return 

# print(count2(12345678910))


     

#reverse

def reverse(num):
    num=abs(num)
    rev=0
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev

print(reverse(991))


def reverse2(num):
    sign=-1 if num<0 else 1

    num=str(abs(num))
    num=num[::-1]
    num=int(num)
    return sign*num



print(reverse2(123412))
print(reverse2(123))
print(reverse2(-123))
print(reverse2(-1623))


def CheckPalindrome(num):
    return str(num) == str(num)[::-1]

print(CheckPalindrome(91919))
