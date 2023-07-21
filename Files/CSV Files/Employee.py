import csv
f=open("Employee.csv","r")
st=csv.reader(f)
L=['Empno','EmpName','Designation','Salary']
print(L)
for rec in st:
    if rec[2].upper()=='ACCOUNTANT' and rec[3]<str(10000):
        print(rec)
f.close()
