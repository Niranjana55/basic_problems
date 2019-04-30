#prime num or not?

import math
def isprime(n):
    Flag=True
    if(n<=1):
        return True
    if(n==2):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            Flag=False
        break
    return Flag

n=int(input("enter the number:"))
print(isprime(n))