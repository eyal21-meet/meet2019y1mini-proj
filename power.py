def power(x, y, z):
    if y > 0:
        power(x, y-1, z*x)
    else:
        print("The answer is " + str(z) + ".")

def calcPower(x, y):
    power(x, y, 1)

x = int(input("Enter the base: "))
y = int(input("Enter the exponent: "))

calcPower(x, y)
