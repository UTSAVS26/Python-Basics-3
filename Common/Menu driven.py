def bfileCreate():
     import pickle
     L=[]
     d={}
     while True:
          d['rollno']=int(input('Enter Roll No. : '))
          d['rname']=input('Enter Name : ')
          d['stream']=input('Enter Stream : ')
          d['percent']=int(input('Enter Percentage : '))
          L.append(d)
          print('Want to add another (yes/no)? ',end=' ')
          choice=input()
          if choice.lower()=='no':
               break
     with open('student.txt','wb') as file:
          pickle.dump(L,file)
     print('File created.....')


def bfileAppend():
     import pickle
     d={}
     file=open('student.txt','rb+')
     L=pickle.load(file)
     d['rollno']=int(input('Enter Roll No. : '))
     d['rname']=input('Enter Name : ')
     d['stream']=input('Enter Stream : ')
     d['percent']=int(input('Enter Percentage : '))
     L.append(d)
     file.seek(0)
     pickle.dump(L,file)
     file.close()
     print('New records appended.....')


def bfileDisplayAll():
     import pickle
     with open('student.txt','rb') as file:
          L=pickle.load(file)
     for x in L:
          print(x)


def bfileSearchStream():
     a=input('Enter Stream: ')
     import pickle
     with open('student.txt','rb') as file:
          L=pickle.load(file)
     for x in L:
          if x['stream'].lower()==a.lower():
               print(x)


def dfileUpdatePercent():
     import pickle
     with open('student.txt','rb') as file:
          L=pickle.load(file)
     a=int(input('Enter existing roll no. : ' ))
     b=eval(input('Enter new percentage: '))
     found=False
     for x in L:
          if x['rollno']==a:
               x['percent']=b
               found=True
               break
     if not found:
          print('Invalid Roll No. ! ; no matching record')
     else:
          file.seek(0)
          pickle.dump(L,file)
          print('Record Updated.....')
     file.close()


def dfileDelete():
     import pickle
     with open('student.txt','rb') as file:
          L=pickle.load(file)
     a=int(input('Enter roll no. of record to be deleted : ' ))
     found=False
     for x in L:
          if x['rollno']==a:
               i=L.index(x)
               found=True
               break
     if not found:
          print('Invalid Roll No. ! ; no matching record')
     else:
          del L[i]
          file.seek(0)
          pickle.dump(L,file)
          print('Record Updated.....')
     file.close()



while True:
     print()
     print("1. Create a File Students.dat")
     print("2. Append Student Record")
     print("3. Display all Students")
     print("4. Display students for a particular stream")
     print("5. Modify percentage of a particular student")
     print("6. Delete a student record")
     print("7. Exit")
     print("Enter your choice: ",end=' ')
     ch=int(input())
     if ch==1:
          bfileCreate()
     elif ch==2:
          bfileAppend()
     elif ch==3:
          bfileDisplayAll()
     elif ch==4:
          bfileSearchStream()
     elif ch==5:
          bfileUpdatePercent()
     elif ch==6:
          bfileDelete()
     elif ch==7:
          print("EXITING THE PROGRAM")
          import sys
          sys.exit()
     else:
          print("Terminating the Program............")
