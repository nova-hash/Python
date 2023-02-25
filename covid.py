import requests

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()
#
# print(mydata)

for i in mydata:
    print(i)

# print('total cases registered on ', mydata["cases_time_series"][199]["date"], "are",
#       mydata["cases_time_series"][199]["dailyconfirmed"])

for i in range(0,len(mydata["cases_time_series"])):
    print(mydata["cases_time_series"][i]["date"] ,"case" ,mydata["cases_time_series"][i]["dailyconfirmed"])

# date = int(input("enter a data : "))
# for i in range(0, len(mydata)):
#     if mydata["cases_time_series"][i]["date"] == date:
#         print(" Name :", mydata[i]["schemeName"])
#         break
#
# else:
#     print("invalid code")
#
