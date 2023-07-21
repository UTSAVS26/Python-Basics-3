def Allinone(SECA,SECB):
    SECA+=SECB
    print(SECA)
A=("Ami","Sam")
B=("om","Ram")
print(A,B)
Allinone(A,B)
print(A)
Allinone(B,A)
print(B)

## Output ##
## ('Ami', 'Sam') ('om', 'Ram') ##
##('Ami', 'Sam', 'om', 'Ram') ##
##('Ami', 'Sam') ##
##('om', 'Ram', 'Ami', 'Sam') ##
##('om', 'Ram')
