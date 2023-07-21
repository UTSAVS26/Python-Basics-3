# Program 3

def createquotes():
    f=open('quotes.txt','w')
    str=''
    while True:
        str=input("Enter a quotes: ")
        str+='\n'
        f.writelines(str)
        print("Do you want to write another?: ",end=' ')
        choice=input()
        if choice.lower()=="no":
            break
    f.close()
createquotes()
print("File Successfully Created!!!")
