# a=10
# b=3
# c=20
# d=-5
# print(complex(a,b)+complex(c,d))
#
# c1=10+2j
# c2=30-1j
# c3=c1+c2
# print(c3)
#
#
# elements=[10,20,30,40,67]
#
# x=bytearray(elements)
# print("original byte array")
# x[0]=33
# for i in x:print(i)
# x[1]=55
#
# print("modified byte array")
# for i in x:print(i)
#
# lst=[10,11,12,12,13,14,10,10]
# s={}
# print("All elements of the list are")
# for ele in lst:
#     print(ele,"\t")
# for ele in lst:
#     cnt=0
#     for ele1 in lst:
#         if(ele==ele1):
#             cnt=cnt+1
#
# if(cnt>=2):
#     s[cnt]=ele
# print("Common element is %i" %ele)
# print("Common element is",s.values(),"is repeated",s.keys(),"times")
# print(s)
#
# import sys
# sum=0
# args=sys.argv
# print("All arguments one by one")
# for x in args:
#  print(x)
# n=len(sys.argv)
# j=1
# while(j<=n-1):
#  y=int(sys.argv[j])
#  if(y%2==0):
#   sum=sum+y
#  j=j+1
# print("Sum is ",sum)

#
# # Initialize array
# arr1 = [1, 2, 3, 4, 5];
#
# # Create another array arr2 with size of arr1
# arr2 = [None] * len(arr1);
#
# # Copying all elements of one array into another
# for i in range(0, len(arr1)):
#  arr2[i] = arr1[i];
#
# # Displaying elements of array arr1
# print("Elements of original array: ");
# for i in range(0, len(arr1)):
#  print(arr1[i]),
#
# print();
#
# # Displaying elements of array arr2
# print("Elements of new array: ");
# for i in range(0, len(arr2)):
#  print(arr2[i]),

# from array import *
#
# x = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = x[2:3]
# print(y)
# y = x[:3]
# print(y)
# y = x[:3]
# print(y)
# y = x[-4:]
# print(y)
# y = x[-4:-2]
# print(y)
# y = x[-4:-1]
# print(y)
# y = x[-5:-1]
# print(y)
# y = x[1:8:2]
# print(y)


def bubbleSort(nlist):
 for passnum in range(len(nlist)-1,0,-1):
  for i in range(passnum):
   if nlist[i]>nlist[i+1]:
    temp = nlist[i]
    nlist[i] = nlist[i+1]
    nlist[i+1] = temp
nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)

