#to findout all factor of N - numbers using whileloop?

number = int(input("Enter the Number: "))
value = 1
print("Factors of a Given Number {0} are:".format(number))

while (value <= number):
    if(number % value == 0):
        print("{0}".format(value))
    value = value + 1
