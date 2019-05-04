
#print all prime numbers 1 to n?
n=int(input("enter the number:"))
for i in range(1,n+1):
    count=0
    for j in range(2,i//2):
        if(i%j==0):
            count=count+1
    if(count<=0):
        print(i)