mylist=[10,20,30,40,50,70,80,90]
mylist[0] = 100
print(mylist)

mylist.append(100)
print(mylist)

copylist = mylist.copy()
print(copylist)

copylist.clear()
print(copylist)

print(mylist.count(30))

print(mylist.extend([120, 130]),mylist)