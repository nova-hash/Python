import requests

url = requests.get("https://api.mfapi.in/mf")
mydata = url.json()


# print(len(mydata))

# for i in range(0 ,len(mydata)):
#     print("Scheme code :",mydata[i]["schemeCode"],",  name :", mydata[i]["schemeName"])



code = int(input("enter a code : "))
for i in range(0 ,len(mydata)):
    if mydata [i]["schemeCode"] == code:
        print(" Name :", mydata[i]["schemeName"])
        break

else:
    print("invalid code")
