#Function to add 5 to a user input number
#The requirements are listed below:
#1. Display the id()of argument before function call.
#2. The function should have one parameter to accept the argument
#3. Display the value and id() of the parameter.
#4. Add 5 to the parameter
#5. Display the new value and id()of the parameter to check
#whether the parameter is assigned a new memory location or
#not.
def incrValue(num):
#id of Num before increment
     print("Parameter num has value:",num,"\nid =",id(num))
     num = num + 5
#id of Num after increment
     print("num incremented by 5 is",num,"\nNow id is ",id(num))
number = int(input("Enter a number: "))
print("id of argument number is:",id(number))           #id of Number
incrValue(number)
