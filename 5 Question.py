# write a program to calulate the electricity bill;


units=int(input("please enter the number of units you consumed in a month"))
if(units<=100):
    payAmount=units*0
elif(units>=101):
    payAmount=(100*0)+(units-100)*5
elif(units<=300):
    payAmount=(100*0)+(200-101)*5+(units-200)*100
else:
    payAmount=0
    fixedcharge=1500.00
Total=payAmount;
print("\nElecticity bill=%.2f" %Total)