#lets try to count digits

def count(num):
     num = abs(num)
     count=0
     if num == 0:
        return 1 
     while(num>0):
          num=num//10
          count=count+1
   
     return count


print(count(34231))



#approach2
def count2(num):
    return len(str(abs(num)))

print(count2(12345678910))

#approach3
def count2(num):
    return 

print(count2(12345678910))


     

