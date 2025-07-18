def printPattern(n):
   for row in range(n):
      for col in range(n):
         print('*', end=' ')
      print()


printPattern(5)