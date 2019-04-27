#check armstrong number(equal to sum of the cubes of its own digits)
#ans : 153 = 1*1*1 + 5*5*5 +3*3*3.
#armstrong num is call narcissistic num

Num=int(input("enter the number:"))
sum=0
temp=Num
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp=temp//10
    
if(Num==sum):
    print("the num is armstrong num:",Num)
else:
    print("the num is not armstrong num:",Num)










