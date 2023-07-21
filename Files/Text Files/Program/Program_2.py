# Program 2

def makefile2():
    '''Store Rollno, Name and Marks of 5 students in a Text File sdetails2.txt'''
    file=open('sdetails2.txt','w')
    for i in range(5):
        rn=int(input("Enter Roll No.: "))
        name=input("Enter Name: ")
        marks=int(input("Enter Marks: "))
        row=(str(rn)+','+name+','+str(marks),'\n') # Row is a tuple type
        file.writelines(row)
    file.close()
makefile2()
print("File Successfully Created!!!")
