import requests

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
mydata = url.json()



for i in mydata:
    print(i)

print("BITCOIN USD PRICE $",mydata["bpi"]["USD"]["rate_float"] )