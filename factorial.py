# fact(no) = no * fact(no-1)
# fact(5)  = 5 * fact(4)
#          = 5 * 4 * fact(3)
#          = 5 * 4 * 3 fact(2)
#          = 5 * 4 * 3 * 2 * fact(1)



def fact(n):
    if (n==0):
        return 1
    else:
        return (n*fact(n-1))


number = int(input("enter a value :"))
sun = fact(number)
print(sun)