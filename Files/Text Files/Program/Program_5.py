# Program 5

def countvowels():
    c=0
    file=open('quotes.txt','r')
    data=file.read()
    lst=data.split()
    for word in lst:
        for char in word:
            if char.lower() in 'aeiou':
                c+=1
    file.close()
    print(data)
    print("No. of Vowels: ",c)
    
countvowels()
