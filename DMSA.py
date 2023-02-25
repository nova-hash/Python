dmsa = input("Enter a symbol of + , -, *, / : ")
first = int(input("Enter a first number : "))
second = int(input("Enter a second number : "))

# add = first + second;
if (dmsa == "+"):
     print("sum of two number : ",first+second)
elif (dmsa == "-"):
     print("sub of two number : ",first-second)
elif (dmsa == "*"):
     print("mul of two number : ",first*second)
elif (dmsa == "/"):
     print("division of two number : ",first/second)
else:
    print("opperater is invalid")




