#fibonacci_sequence
a=0
b=1
temp=0
n=int(input("enter the num :"))
while(a<n):
    temp=a+b
    a=b
    b=temp
print("temp",temp)
