import os
def countand():
    if os.path.isfile("status.txt"):
        fob=open("status.txt","r")
        c=0
        while True:
            Str=fob.readline()
            print("Lines in File are : ")
q            print(Str)
            if not Str:
                break
            Str=Str.rstrip().lower().split()
            for i in range(len(Str)):
                if(Str[i]=='and' or Str[i]=='AND'):
                    c=c+1
        print("Count of \'and\' in file is/are : ",c)
    else:
        print("File does not exist.")
countand()
