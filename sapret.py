word = input("enter a word");

symbol = input("enter a symbol to sepret");

for i in (word):
    print(i  ,end=symbol)

print("\n==================================================================================================")

for i in (word):
    if(i == symbol):
        print()
    else:
        print(i ,end="")










