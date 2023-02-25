import requests

url = requests.get("https://inshorts.deta.dev/news?category=sports")
mydata = url.json()

# print(mydata)

for i in mydata:
    print(i)

print("total news ",len(mydata["data"]))

for i in range(0, len(mydata["data"])):
    print(i+1," - ",mydata["data"][i]["title"], " (",mydata["data"][i]["date"], mydata["data"][i]["time"],")")



