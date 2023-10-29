a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Please enter valid values.", err)
else:
    print("Both values were valid.")
finally:
    print("Finally!")
