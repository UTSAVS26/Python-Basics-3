#Function to display mixed fraction for an improper fraction
#The requirements are listed below:
#1. Input numerator and denominator from the user.
#2. Check if the entered numerator and denominator form a proper
#fraction.
#3. If they do not form a proper fraction, then call
#mixedFraction().
#4. mixedFraction()display a mixed fraction only when the fraction
#does not evaluate to a whole number.
def mixedFraction(num,deno = 1):
     remainder = num % deno
     #check if the fraction does not evaluate to a whole number
     if remainder!= 0:
          quotient = int(num/deno)
          print("The mixed fraction=", quotient,"(",remainder, "/",deno,")")
     else:
          print("The given fraction evaluates to a whole number")
#function ends here
num = int(input("Enter the numerator: "))
deno = int(input("Enter the denominator: "))
print("You entered:",num,"/",deno)
if num > deno:       #condition to check whether the fraction is improper
     mixedFraction(num,deno)       #function call
else:
     print("It is a proper fraction")
