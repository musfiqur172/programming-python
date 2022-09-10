number = input("Please enter a number: ")
number = int(number)

if number > 0:
    print(number, "is a positive number")
elif number < 0:
    print(number, "is a negative number")
else:
    print(number, "is zero")