# Swap two numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Before swap: a =", a, ", b =", b)

a, b = b, a  # Pythonic swap
print("After swap: a =", a, ", b =", b)
