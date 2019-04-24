#check leap year or not
year=int(input("enter the year:"))
if((year%4==0)or(year%100==0)and(year%400==0)):
    print("Leapyear")
else:
    print("non Leapyear")

