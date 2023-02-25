# number = int(input("Enter a number : "))
#
# for i in range(2 , number + 1 ):
#     if i > 1:
#         print(i,"i>1")
#
#         for j in range( 2, i):
#             print(j,"ran")
#             if(i % j) == 0:
#                 break
#         else:
#             k == i;
#             print( k,"pr")
#
#     else:
#         print("not")

# WRITE A PROGRAM TO SWAP A TWO VARIABLE

# 1 USING TEMP VARIABLE

P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To swap the value of two variables
# we will user third variable which is a temporary variable
temp_1 = P
P = Q
Q = temp_1

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)

# 2 USING NOT TEMP VARIABLE

x=int(input("Enter x:"))
y=int(input("Enter y:"))


# Method 1
x=x+y
y=x-y
x=x-y

print("The Value of X after swapping: ", x)
print("The Value of Y after swapping: ", y)
print(x,y)






