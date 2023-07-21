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
     with open('student.dat','wb') as file:
          pickle.dump(L,file)
print('File created.....')
