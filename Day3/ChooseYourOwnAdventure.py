#Treasure Island Game!
print("Welcome to Treasure Island! Your mission is to find the treasure!")
decision1 = input("Left or Right? ").lower()
if decision1 == "right":
    print("GAME OVER!")
    exit(0)

decision2 = input("Swim or Wait? ").lower()
if decision2 == "swim":
    print("GAME OVER!")
    exit(0)

decision3 = input("Which door will you choose? Red, Blue or Yellow? ").lower()
if decision3 == "yellow":
    print("You Win! *applause*")
else:
    print("GAME OVER!")
    exit(0)