import random
from array import array


def main():
    n = int(input("Enter the number of card types:")) 
    x = array('i', [1, 0])  
    count = 0 
    distinct = 0  
    while distinct < n:
        value = int((random.randint(0, n)) * n-1) 
        print("Random Number Generated:\t", value)
        count = count + 1
        print("Count of each random Number:\t", count)
        res = isCollected(value, n)
        y = x[res]
        if not y:
            distinct = distinct + 1
        print("The total number of cards collected =\t", count)

#  Checking the random numbers

def isCollected(value, n):
    if value <= n:
        return 1
    else:
        return 0


main()