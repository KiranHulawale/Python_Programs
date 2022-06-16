import math
value = 1

while value == 1:
    try:
        t = int(input("Enter the tempreture in Fahrenheit\n"))
        v = int(input("Enter the speed miles per hour\n"))
        if t < 0 or v < 0 :
            raise ValueError

        if(t > 50) | (v > 120) | (v < 3):
            print("Formula is not valid.Kindly give valid input")
        else:
            w = (int) (35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * math.pow(v , 0.16 ))
            print("The National Weather Service defines the effective tempreture (the wind chill) to be :" ,w,"Degree ")
            break
    except ValueError:
        print("Enter the positive number")
    break