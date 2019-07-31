def factorial(x, y, z):
    if y <= x:
        z *= y
        y += 1
        factorial(x, y, z)
    else:
        print("The factorial of " + str(x) + " is " + str(z) + ".")
def calcFactorial(x):
     factorial(x, 1, 1)
   

x = int(input("Pick a number: "))

calcFactorial(x)
