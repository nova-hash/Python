cp = float(input("Enter the cost price of the bike:") )
if cp > 100000:
     t = 0.15
elif cp > 50000 and cp <= 100000:
    t = 0.10
elif cp <= 50000:
    t = 0.05
rt = (cp * t)+ cp
print(rt, " is the road tax to be paid.")
