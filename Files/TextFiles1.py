def createfile():
    f = open("Notes.txt","a+")
    n = int(input("Enter no. of lines you want to enter: "))
    for i in range(n):
        ln = input("Enter Line: ")
        f.write(ln)
        f.write('\n')
    f.close()

def count_alphabets():
    f = open('Notes.txt','r')
    data = f.readlines()
    count=0
    for line in data:
        if line[0] == "A" or line[0] == "P":
            count += 1
    f.close()
    print("No. of lines starting with A and P are: ",count)

def count_cases():
    f = open("Notes.txt","r")
    data = f.read()
    lst = data.split()
##    vowels = 0
##    vwl = []
##    consonents = 0
##    cns = []
    lowercase = 0
    digits = 0
    for word in lst:
        for char in word.split():
##            if char.lower() in "aeiuo":
##                vowels += 1
##                vwl.append(char)
            if char in "abcdefghijklmnopqrstuvwxyz":
                lowercase += 1
                print(char)
            elif char in "1234567890" :
                digits += 1
            else:
                continue
    print("Total No. of Lowercase Character: ",lowercase)
    print("Total No. of Digits: ",digits)
    print('\n')
    f.close()

##def count_lines():
##    f = open("TextFiles.txt","r")
##    data = f.read()
##    lst = len(data)
##    print("Total No. of Lines are: ",lst)
##    print(data)

found = True
while True:
    print("\t\tText File Handling.")
    print("\t1. Create File.")
    print("\t2. Count Lowercase and Digits.")
    print("\t3. Count Words Starting from A or P.")
    print("\t4. Exit")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        createfile()
    elif ch == 2:
        count_cases()
    elif ch == 3:
        count_alphabets()
    elif ch == 4:
        break
