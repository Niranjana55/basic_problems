#print all numbers is a range divisible by a given number

Lower=int(input("enter the lower range:"))
Upper=int(input("enter the upper range:"))
N=int(input("divisible by:"))
for i in range(Lower,Upper+1):
    if(i%N==0):
        print(i)