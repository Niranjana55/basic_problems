a=int(input("enter the num a:"))
b=int(input("enter the num b:"))
n=int(input("enter the num of terms :"))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1