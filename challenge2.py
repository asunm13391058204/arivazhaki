def lp(year):
 if(year%400==0 and year%100!=0):
    return True
 elif(year%400==0):
    return True
 else:
   return False
year=int(input("enter a year:"))
if lp(year):
  print(year,"is a leap year")
else:
  print(year,"not a leap year")