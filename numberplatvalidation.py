# import re
number = input("Enter vehicle number")

digitcount = 0
capcount = 0

# GJ01AH2213
if len(number)==10:
    # for i in number:
    #     if ord(i) >= 65 and ord(i) <= 90:
    #         capcount = capcount + 1
    #         if ord(i) >= 48 and ord(i) <= 57:
    #             digitcount = digitcount + 1
    #             if ord(i) >= 65 and ord(i) <= 90:
    #                 capcount = capcount + 1
    #                 if ord(i) >= 48 and ord(i) <= 57:
    #                     digitcount = digitcount + 1
    # # r = re.compile('[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}')
    # # if r.match(number):
    if (number [0:2].isalpha() and number[2:4].isdigit() and number [4:6].isalpha() and number[6:].isdigit()):
        print("vaild vehicle number")
    else:
        print("vehicle number is not right")
else:
    print("not valid vehicle number")

#===================================================================================================
for i in [0,1,4,5]:
    if ord(number[i]) >= 65 and ord (number[i]) <= 90:
        capcount = capcount + 1
for i in [2,3,6,7,8,9]:
    if ord(number[i]) >= 48 and ord(number[i]) <= 57:
        digitcount = digitcount + 1

if capcount == 4 and digitcount == 6:
    print("valid number plate")
else:
    print("Please enter a valid number plate")
