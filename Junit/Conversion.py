def c_2_f(c):
    c = [c * (9 / 5) + 32]  #formula (c = c*9/5+32)
    return c


def f_2_c(f):
    f = (f - 32) * (5 / 9)  #formula (f = (f-32)*(5/9)))
    return f


def main():
    value = int(input("Enter the value:"))  
    op = int(input("Enter 1 for  celsius conversion \n 2 for Fahrenheit Conversion\n"))
    if op == 1:
        print(value, " is converted to Celsius : ", f_2_c(value))
    elif op == 2:
        print(value, " is converted to Fahrenheit : ", c_2_f(value))
    else:
        print("Invalid Input")


main()