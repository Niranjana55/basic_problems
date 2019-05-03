#sum of first n natural numbers 
num=int(input("enter the number:"))
hold=num
sum=0
if num<=0:
    print("enter a whole positive num:")
else:
    while(num>0):
        sum=sum+num
        num=num-1
    print("sum of first",hold,"natural number is:",sum)
    