#calculate the average of numbers in a given list
n=int(input("enter the num of elements:"))
a=[]
for i in range(0,n):
    element=int(input("enter the element:"))
    a.append(element)
avg=sum(a)/n
print("average of elements in the list",round(avg,2))
