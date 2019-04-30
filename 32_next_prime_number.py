#next prime number?

import math
def isprime(n):
    flag=True
    if(n<=1):
        return True
    if(n==2):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            flag=False
        break
    return flag

def nextprime(n):
    count=0
    i=n+1
    while(count<1):
        if(isprime(i)):
            return i
        i+=1
    
n=int(input("enter the number:"))
print(nextprime(n))