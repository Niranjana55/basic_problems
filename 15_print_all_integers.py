#print all integers that aren't divisible by either 2 or 3 and lie b/w 1 and 50?

for i in range(1,51):
    if(i%2!=0 and i%3!=0):
        print(i)