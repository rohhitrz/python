def patternPrint6(n):
    for row in range(n):
        for col in range(1,n-row+1):
            print(col,end='')
        print()


patternPrint6(5)