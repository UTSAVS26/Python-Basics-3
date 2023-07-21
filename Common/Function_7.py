def pos1(n):
     if n>0:
          return int(str(n)[-1])
     else:
          print('please enter a non-zero positive integer')
a=int(input('enter a positive number:'))
print(pos1(a))
