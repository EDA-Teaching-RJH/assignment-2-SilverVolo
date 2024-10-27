### Part Two -- your code goes here. 
import random

numRand = random.randint(1,100)
flag = True

while flag:
    num = False
    while not num:
        try:
            guess = int(input("Input your guess: "))
        except:
            print("Please only input numbers")
        else:
            num = True
    
    if guess == numRand:
        print("Correct you have found the number")
        flag  = False
    else:
        print("Incorrect please try again.")