#I have created a program that calculates the sum and tells the score

import random

score = 0

while(True):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    
    actual_sum = a + b

    user_sum = int(input(f"{a} + {b} \n"))
    if user_sum == actual_sum:
        score += 1
    else:
        print(f"Your score is: {score}")
        exit()
    