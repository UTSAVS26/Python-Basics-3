#Program to calculate income tax of an employee
basic=int(input("Enter the basic salary:"))
savings=int(input("Enter the total savings made:"))
if basic<=250000:
     tax=0
elif basic<=500000:
     if savings>150000:         #Assessing the maximum savings limit
          savings=150000
     tot_income=basic-savings-250000   #Total taxable income after all the deductions
     tax=tot_income*0.05       #Total tax after calculations
elif basic<=1000000:
     if savings>150000:
          savings=150000
     tot_income_5slab=500000-savings-250000    #Total income under 5% slab
     tot_income_20slab=basic-500000   #Total income under 20% slab
else:
     if savings>150000:
          savings=150000
     tot_income_5slab=500000-savings-250000   #Total income under 5% slab
     tot_income_30slab=basic-1000000   #Total income under 30% slab
     tax=tot_income_5slab*0.05+tot_income_30slab*0.03+100000  #100000 is for 20% slab from
                                                                                                #50000 to 1000000 tax calculated

print("Total income tax to be paid= ",tax)
