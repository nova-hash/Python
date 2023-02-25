password = input("Enter a password : ")
digitcount = 0
capcount = 0
spicalchatercount = 0

if len(password)>=8 and len(password)<=12:
   for i in password:
      if ord(i) >= 48 and ord(i) <= 57:
         digitcount = digitcount + 1
      elif ord(i)>=65 and ord(i)<=90:
          capcount = capcount + 1
      elif ord(i) == 36 or ord(i) == 64:
         spicalchatercount = spicalchatercount + 1

   if digitcount >=1 and spicalchatercount >=1 and capcount >=1:
      print("vaild password")
   else:
      print("password must contain atleast one capital, one digit and one spicial char ")
else:
   print("password must be 8 to 12 characters long")