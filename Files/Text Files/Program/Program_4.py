# Program 4

def countlines():
    file=open('quotes.txt','r')
    data=file.readlines()
    print(data)
    count=0
    for line in data:
        if line[0]=="A" or line[0]=="a":
            count+=1
    file.close()
    print("No. of lines atarting with A/a are: ",count)
    
countlines()
