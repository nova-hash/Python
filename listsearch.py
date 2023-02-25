mydata = ['ahmedabad', 'surat','rajkot']
uservalue = input("enter city name")


for i in mydata:
    if uservalue == i:
        print("city found")
        break
else:
    print("city is not found")