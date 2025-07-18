def printPattern2(n):
    for row in range(1,n+1):
        for col in range(row):
            print("*",end=' ')
        print()
   

printPattern2(5)