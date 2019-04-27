#fibonacci_sequence
a=0
b=1
c=0
n=int(input("enter the num :"))
while(a<n):
    c=a+b
    a=b
    b=c
print(c)
