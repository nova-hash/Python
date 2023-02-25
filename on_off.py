userinput = ''
status = "off"
while userinput != 'quit':
    userinput = input("enter on/off quit : ")
    if userinput == "off":
        if status == "off":
            print("ac is already off")
        else:
            print("ac is off now")
            status = "off"
    elif userinput == "on" :
        if status=="on":
            print("ac is already on")
        else:
            print("ac is on now")
            status = "on"