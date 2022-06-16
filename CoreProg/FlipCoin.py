import random

n = 0
def flipCoin():
    heads = 0  
    tails = 0  
    headspercent = 0  
    tailspercent = 0  
    n = int(input("How many times you want to Flip Coin?"))
    if n >= 0:
        for i in range(n):  
            coin = random.randint(0, 1) 

            if coin == 0:  
                heads += 1  
            else:  # if coin value is assigned something other than 1
                tails += 1 

            headspercent = ((heads / (heads + tails)) * 100) 
            tailspercent = ((tails / (heads + tails)) * 100) 

        print("Heads percent: " + str(headspercent)) 
        print("Tails percent: " + str(tailspercent))  
    else:
        print("Enter the positive Number:")

flipCoin()