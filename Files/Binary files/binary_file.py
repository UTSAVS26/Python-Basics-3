#create a binary file
import pickle
def insertRec():
     record=[]
     while True:
          roll_no=input("Enter Student roll no : ")
          name=input("Enter Student name: ")
          marks=input("Enter the marks obtained: ")
          rec=[roll_no,name,marks]
          record.append(rec)
          ch=input("Want to add More Records: ")
          if ch.upper()=='N':
               break
     f=open("student.dat","wb")
     pickle.dump(record,f)
     print("file created....")
     f.close()

def readRec():
     f=open("student.dat","rb")
     stud_rec=pickle.load(f)
     print("Contents of Student File are: ")
     for R in stud_rec:
          roll_no=R[0]
          name=R[1]
          marks=R[2]
          print(roll_no,name,marks)
     f.close()

def searchRec():
     f=open("student.dat","rb")
     stud_rec=pickle.load(f)
     found=0
     rno=input("Enter the Roll No. to Search: ")
     for R in stud_rec:
          if R[0]==rno:
               print("Succesful Search",R[1],"Found!")
               found=1
               break
     if found==0:
          print("Sorry, Record Not Found")
     f.close()

def updateMarks():
     f=open("student.dat","rb+")
     stud_rec=pickle.load(f)
     found=0
     rollno=input("Enter the Roll No. to Update Marks: ")
     for R in stud_rec:
          rno=R[0]
          if rno==rollno:
               print("Current Marks is: ",R[2])
               R[2]=input("New Marks: ")
               found=1
               break
     if found==1:
          f.seek(0)
          pickle.dump(stud_rec,f)
          print("Marks Updated!!!")
     f.close()



while True:
     print("Type 1 to Insert Record.")
     print("Type 2 to Display Record.")
     print("Type 3 to Search Record.")
     print("Type 4 to Update Record.")
     choice=int(input("Enter your choice: "))
     if choice==1:
          insertRec()
     elif choice==2:
          readRec()
     elif choice==3:
          searchRec()
     elif choice==4:
          updateMarks()
     yn=input("Wish to Continue (Y/N): ")
     if yn.upper()=="N":
          break

