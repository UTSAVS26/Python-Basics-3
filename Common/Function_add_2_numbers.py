#Function to add two numbers
#The requirements are listed below:
#1. We need to accept 2 numbers from the user.
#2. Calculate their sum
#3. Display the sum.
#function definition
def addnum():
     fnum = int(input("Enter first number: "))
     snum = int(input("Enter second number: "))
     sum = fnum + snum
     print("The sum of ",fnum,"and ",snum,"is ",sum)
#function call
addnum()
