import requests
api1 = "https://inshorts.deta.dev/news?category="
api2 = input("Enetr a category : ")
api = api1+api2

url = requests.get(api)
mydata = url.json()

print(mydata)

# for i in mydata:
#     print(i)
#
# print("total news ",len(mydata["data"]))
print("===========================================letest news=====================================================")
for i in range(0, len(mydata["data"])):
    print(i+1," - ",mydata["data"][i]["title"], " (",mydata["data"][i]["date"], mydata["data"][i]["time"],")")



