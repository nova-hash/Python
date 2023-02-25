my_list = ['apple', 'mango', 'pineapple', 'kivi']
user = input("enter a fruit name : ")
for i in range(0, len(my_list)):
    if user == my_list[i]:
        print("in this list")
        break;
else:
    print('not in list')




