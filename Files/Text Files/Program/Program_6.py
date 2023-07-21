# Program 6

file=open('greet.txt','w')
file.write("Hello World")
file.close()

file=open('greet.txt','r+')
print(file.tell())
print(file.read(2))
print(file.tell())
print(file.read(5))
print(file.tell())
file.seek(3,0)
print(file.tell())
file.seek(0,2)
print(file.tell())
file.close()
