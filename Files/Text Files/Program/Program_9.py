# Program 9

def puretext():
    with open("wrongmother.txt",'r') as file:
        content=file.read()

    content=content.replace('He','She')

    with open("correctmother.txt",'w') as file:
        file.writelines(content)
puretext()
