
#Print the first “N” prime numbers starting from 2.
#n=7
#2,3,5,7

i=1
n = int(input("Enter the number:"))
for k in range (1, (n+1), 1):
    count=0
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0):
            count = count+1

    if (count==2):
          print (i)
    else:
          k = k-1

    i=i+1
