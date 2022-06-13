import random

while True:
    choices = ["r", "p", "s"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("r, p, or s?:").lower()

    if player == computer:

        print("computer: ", computer)
        print("player: ", player)
        print("It's a Tie")
    elif player == "r":
        if computer == "p":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "s":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "s":
        if computer == "r":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "p":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "p":
        if computer == "s":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "r":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    play_again = input("Play againh? (yes/no): ").lower()

    if play_again != "yes":
        break
    
print("Bye!")
