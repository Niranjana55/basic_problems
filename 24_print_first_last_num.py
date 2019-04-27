import random
a=[]
for i in range(0,10):
    x=(random.randint(0,10))
    a.append(x)
print(a)
print("first number",a[0])
print("last number",a[-1])