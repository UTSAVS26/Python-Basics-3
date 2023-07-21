#Function to calculate mean
#The requirements are listed below:
#1. The function should have 1 parameter (list containing floating
#point values)
#2. To calculate mean by adding all the numbers and dividing by
#total number of elements
def myMean(myList): #function to compute means of values in list
     total = 0
     count = 0
     for i in myList:
          total = total + i #Adds each element i to total
          count = count + 1 #Counts the number of elements
     mean = total/count #mean is calculated
     print("The calculated mean is:",mean)
myList = [1.3,2.4,3.5,6.9]
#Function call with list "myList" as an argument
myMean(myList)
