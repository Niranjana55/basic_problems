number = int(input(" Enter the Number: "))

for value in range(1, number + 1):
    if(number%value == 0):
        print("{0}".format(value))