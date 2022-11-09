#Rock_Paper_Scissors game:
import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False
    
    

print("Comp's turn: Rock(r) Paper(p) Scissors(s)?: ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"


you = input("Your turn: Rock(r) Paper(p) Scissors(s)?: ")
print(f"Computer chose: {comp}")
print(f"You chose: {you}")

a = gameWin(comp, you)

if a == None:
    print("The game is tie!🤣")
elif a:
    print("You won!😉")
else:
    print("You lose!😝")
