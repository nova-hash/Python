
# WRITE A PROGRAM TO SWAP A TWO VARIABLE

print(" 1 USING TEMP VARIABLE")

Q = int(input("Please enter value for Q: "))

# To swap the value of two variables
# we will user third variable which is a temporary variable
temp_1 = P
P = Q
Q = temp_1

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)

print(" 2 USING NOT TEMP VARIABLE")

x=int(input("Enter x:"))
y=int(input("Enter y:"))


# Method 1
x=x+y
y=x-y
x=x-y

print("The Value of X after swapping: ", x)
print("The Value of Y after swapping: ", y)







