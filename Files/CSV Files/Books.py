import csv
F = open("book.csv","w",newline='')
St = csv.writer(F,delimiter='@')
ans='y'
while ans.upper()=='Y':
    code=input("Enter Book Code: ")
    name=input("Enter Book Name: ")
    author=input("Enter Book Author: ")
    price=float(input("Enter Book Price: "))
    List=[code,name,author,price]
    St.writerow(List)
    ans=input("Want to add more Book details in file (Y/N): ")
F.close()
