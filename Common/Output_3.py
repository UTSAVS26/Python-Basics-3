def FLName(First,Last):
    First+=(" "+Last)
    print(">>",First)
F,L="Ami","Virk"
print("#",F,L)
FLName(F,L)
print("#",F)
FLName(L,F)
print("#",L)

## Output ##
## # Ami Virk ##
## >> Ami Virk ##
## # Ami ##
## >> Virk Ami ##
## # Virk ##
