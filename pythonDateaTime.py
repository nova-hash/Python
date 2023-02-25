# %a.%A,%b,%B,%y,%Y,%H,%I,%p,%j,%U,%X,%n
import datetime;
import os
import time

dt = datetime.datetime.now();
print(dt);

output1 = dt.strftime("%a"); #short current day
print("a",output1);

output2 = dt.strftime("%A"); #full current day
print("A",output2);

output3 = dt.strftime("%b"); #short current month
print("b",output3);

output4 = dt.strftime("%B"); #full current month
print("B",output4);


output5 = dt.strftime("%y"); #short current year
print("y",output5);

output6 = dt.strftime("%Y"); #full current year
print("Y",output6);

output7 = dt.strftime("%H"); # current hours 24
print("H",output7);

output8 = dt.strftime("%I"); # current hours am,pm
print("I",output8);

output9 = dt.strftime("%p"); #short current date
print("p",output9);

output10 = dt.strftime("%j"); #365 of days
print("j",output10);

output11 = dt.strftime("%U"); #54 of weeks
print("U",output11);

output12 = dt.strftime("%X"); #full current time
print("X",output12);

output13 = dt.strftime("%w"); #day of number
print("w",output13);



print("=========================================")
while True:
    os.system("cls")
    present = datetime.datetime.now()
    future = datetime.datetime(2022, 9, 28, 0, 0, 0)
    difference = future - present
    print(difference)
    time.sleep(1)