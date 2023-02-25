import datetime;
import os;
import time;


dt = datetime.datetime.now()
d = dt.day

m = dt.month
if d==25 and m==12:
    print("TODAY IS CHRISTMAS")
else:
    print("TODAY NOT CHRISTMAS")

print("----------------------------------------------")
y = dt.year
if m==9:
    if d>=23 and d<=30:
        print("big billion days live now")
print("=============================================")
print("<---===TASK===--->")
#every weeks of wednesday and firday buy one get one free;
d = int(dt.strftime("%w"))
if d==3 or d==5:
    print("buy one get one free")
else:
    print("Today is regual price")

print("-------------------------------------------------")
#every sunday 4 to 6 pm 50% off
h = int(dt.hour)
d = int(dt.strftime("%w"))
if d==6:
    if h >= 16 and h <= 18:
        print("time to 50% off")
else:
    print("regual price")
print("-------------------------------------------------")
#12 o=clock sale starts in 5 hours 15 min and 20 seconds
# while True:
#     os.system("cls")
#     present = datetime.datetime.now()
#     future = datetime.datetime(2022, 9, 28, 0, 0, 0)
#     difference = future - present
#     print(difference)
#     time.sleep(1)






