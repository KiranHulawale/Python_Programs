x=int(input("Enter the year to find it's a leap year or not::"))
if (x%4) == 0:
   if (x%100) == 0:
       if (x%400) == 0:
           print("{} is a leap year".format(x))
       else:
           print("{} is not a leap year".format(x))
   else:
       print("{} is a leap year".format(x))
else:
   print("{} is not a leap year".format(x))