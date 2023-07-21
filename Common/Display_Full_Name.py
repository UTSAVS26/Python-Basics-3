#Function to display full name
#The requirements are listed below:
#1. The function should have 2 parameters to accept first name and
#last name.
#2. Concatenate names using + operator with a space between first
#name and last name.
#3. Display full name.
def fullname(first,last):
     #+ operator is used to concatenate strings
     fullname = first + " " + last
     print("Hello",fullname)
#function ends here
first = input("Enter first name: ")
last = input("Enter last name: ")
#function call
fullname(first,last)
