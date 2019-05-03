#number of prime number between m and n 
lower=int(input("enter the number m:"))
upper=int(input("enter the number n:"))
for i in range(lower,upper+1):
    if(i>1):
        for num in range(2,i):
            if(i%num==0):
                break
        else:              
            print (i)



        
