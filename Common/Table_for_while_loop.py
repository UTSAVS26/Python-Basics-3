#Program to dislplay the table using
#for loop and while loop.

n=int(input("Enter the number to display the table: "))
#for loop
for i in range(1,11):
     print(n,"\tX\t",i,"\t=\t",n*i)
print()
     
#while loop
i=1
while i<11:
     print(n,"\tX\t",i,"\t=\t",n*i)
     i+=1
