# Program to reverse a user defined string.
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = input("Enter String: ") 
print ("The original string  is : ",s)   
print ("""The reversed string using extended slice
       operator  is : """,reverse(s))  
