# Program 1

def makefile():
    '''Store Rollno, Name and Marks of 5 students in a Text File sdetails.txt'''
    file=open('sdetails.txt','w')
    for i in range(5):
        rn=int(input("Enter Roll No.: "))
        name=input("Enter Name: ")
        marks=int(input("Enter Marks: "))
        row=str(rn)+','+name+','+str(marks)
        file.write(row+'\n')
    file.close()
makefile()
print("File Successfully Created!!!")
