def patternPrint5(n):
    for row in range(n):
        for col in range(n-row):
            print("*",end='')
        print()


patternPrint5(5)