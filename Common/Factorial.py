#Function to calculate factorial
#The requirements are listed below:
#1. The function should accept one integer argument from user.
#2. Calculate factorial. For example:
#3. Display factorial
def calcFact(num):
     fact = 1
     for i in range(num,0,-1):
          fact = fact * i
     print("Factorial of",num,"is",fact)
num = int(input("Enter the number: "))
calcFact(num)
