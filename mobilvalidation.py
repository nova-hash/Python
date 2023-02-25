mobile = input("Enter moblie number : ")
digitcount = 0

if len(mobile) == 10:
    for i in mobile:
        if ord(i)>=48 and ord(i)<=57:
            digitcount = digitcount + 1

    if digitcount == 10:
        if mobile[0]=='6' or mobile[0]=='7' or mobile[0]=='8' or mobile[0]=='9':
            print("valid mobile number ")
        else:
            print("mobile number must be start with 6,7,8 or 9")
    else:
        print("all must be digits")
else:
    print("mobile number must be in 10 digits long")
