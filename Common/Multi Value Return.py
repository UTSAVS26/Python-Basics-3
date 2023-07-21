def Something(SomeParameter):
     #Some Expressions
     Var1=SomeParameter*5
     Var2=SomeParameter*3
     return Var1,Var2
P=input("Some Value: ")
V1,V2=Something(P)
print(V1)
print(V2)
V1,V2=Something(50)
print(V1,V2)
