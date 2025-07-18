def patternPrint7(n):
    for row in range(1,n+1):
        for col in range(2*row-1):
            print('*',end='')
        print()


patternPrint7(5)