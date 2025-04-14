import random

human_rps_choices = [1, 2, 3]

computer = random.randint(0, 2)
human = int(input("What will you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors?"))

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

if human >=3 or human < 0:
    print("You typed an invalid number. You lose!")

elif human == 0 and computer == 2:
    print("You win!")
elif    computer == 0 and human ==2:
    print("You lose!")
elif computer > human:
    print("You lose!")
elif computer == human:
    print("It's a draw!")
