import requests
api1 = "https://api.postalpincode.in/pincode/"
api2 = input("Enetr a pincode : ")
api = api1+api2

url = requests.get(api)
mydata = url.json()
print(mydata)

for i in mydata:
    print(i)

# print("total news ",len(mydata))

for i in range(0, len(mydata)):
    print(i+1," - ",mydata[i]["PostOffice"][i]["Name"] )
