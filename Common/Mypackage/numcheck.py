import math
def even(num):
      if num%2==0:
            return 1
      else:
            return 0

def isprime(num):
      for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                  return o
      return 1

def palindrome(num):
      mynum=num
      n=0
      while num!=0:
            r=num%10
            n=n*10+r
            num=num//10
      if mynum==n:
            return 1
      else:
            return 0
