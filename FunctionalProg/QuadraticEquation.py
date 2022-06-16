import math

name = input("Enter your name :\n ")  
print("Hi, '", name, "'.")
print(name, ", you are here for finding the real and imaginary roots")
print("\n Equation is 'Ax*x + Bx + C' ")
print("\n Please give the following details:")

try:
    a = int(input(" Enter the value of 'A' : \n ")) 

    b = int(input(" Enter the value of 'B' : \n ")) 

    c = int(input(" Enter the value of 'C' : \n ")) 

    if a != 0:
        d = (b * b) - (4 * a * c)  
        if d > 0: 
            root1 = float((-b + math.sqrt(d)) / (2 * a))  
            root2 = float((-b - math.sqrt(d)) / (2 * a)) 
            print(" root1 = %.2f", root1, " and root2 = %.2f", root2)
        elif d == 0: 
            root1 = root2 = -b / (2 * a) 
            print(" root1 = root2 = ", root1)
        else:
            realPart = float(-b / (2 * a))  
            imaginaryPart = float(math.sqrt(-d) / (2 * a))  
            print(" root1 = ", realPart, " + ", imaginaryPart, " i")
            print()
            print(" root2 = ", realPart, " - ", imaginaryPart, " i")
except ValueError:
    print(" Enter the Numeric value ")
except ZeroDivisionError:
    
    print(" Division by Zero Error ")