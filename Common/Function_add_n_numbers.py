#Program to find the sum of first n natural numbers
#The requirements are:
#1. n be passed as an argument
#2. Calculate sum of first n natural numbers
#3. Display the sum
#function header
def sumSquares(n): #n is the parameter
     sum = 0
     for i in range(1,n+1):
          sum = sum + i
          print("The sum of first",n,"natural numbers is: ",sum)
num = int(input("Enter the value for n: "))
#num is an argument referring to the value input by the user
sumSquares(num)           #function call
