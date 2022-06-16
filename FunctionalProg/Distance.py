import math
x = float(input("Enter the X Co-ordinate:"))  
y = float(input("Enter the Y Co-ordinate:"))  
distance = math.sqrt(x*x + y*y)  
print(" The Euclidean Distance from origin '",x,"' and '",y,"' is '",distance,"'")