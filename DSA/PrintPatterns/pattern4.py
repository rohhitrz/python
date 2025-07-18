def patternPrint4(n):
    for row in range(1,n+1):
        for col in range(row):
            print(row,end="")
        print()


patternPrint4(5)