#Find Numbers Divisible by Another Number
my_list = [12, 65, 54, 39, 102, 339, 221,]
n=int(input("enter the num:"))
result = list(filter(lambda x: (x % n == 0), my_list))
print("Numbers divisible by n are",result)