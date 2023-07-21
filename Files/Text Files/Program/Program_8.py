# Program 8

def filedel():
    with open('quotes.txt','r') as file:
        L= file.readlines()
        file.close()
        print(L)
        del L[0]
        print(L)
    file=open("quotes1.txt","w")
    file.writelines(L)
    file.close()
filedel()
