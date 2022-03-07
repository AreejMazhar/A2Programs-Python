import random
import sys

# initialize the wins, losses and ties
wins = 0
losses = 0
ties = 0

print("Let's play Rock, Paper, Scissors! Here are the rules:")
print(">Rock beats Scissors")
print(">Scissors beats Paper")
print(">Paper beats Rock")

while True:  # main game loop
    while True:  # player input loop
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        PlayerMove = input('Enter you move: (r)ock, (p)aper, (s)cissors, or (q)uit: ')
        if PlayerMove == 'q':
            print("Thank you for playing!")
            sys.exit()   # exits the program
        if (PlayerMove == 'r') or (PlayerMove == 'p') or (PlayerMove == 's'):
            break  # break out of loop
        else:
            print("Type one of r, p, s or q please!")

    # Display of player's choice
    if PlayerMove == 'r':
        print("ROCK versus...")
    elif PlayerMove == 'p':
        print("PAPER versus...")
    elif PlayerMove == 's':
        print("Scissors versus...")

    # Choose and Display computer's choice
    ComputerMove = " "
    RanNum = random.randint(1, 3)
    if RanNum == 1:
        ComputerMove = 'ROCK'
    elif RanNum == 2:
        ComputerMove = 'PAPER'
    elif RanNum == 3:
        ComputerMove = 'SCISSORS'
    print(ComputerMove)

    # Display Wins, Losses, Tie
    if (PlayerMove == 'p') and (ComputerMove == 'PAPER'):
        print('It\'s a tie!')
        ties = (ties + 1)
    elif (PlayerMove == 's') and (ComputerMove == 'SCISSORS'):
        print('It\'s a tie!')
        ties = (ties + 1)
    elif (PlayerMove == 'r') and (ComputerMove == 'ROCK'):
        print('It\'s a tie!')
        ties = (ties + 1)
    elif (PlayerMove == 'p') and (ComputerMove == 'ROCK'):
        print("That's a win for you!")
        wins = (wins + 1)
    elif (PlayerMove == 'p') and (ComputerMove == 'SCISSORS'):
        print("Aw you lost.")
        losses = (losses + 1)
    elif (PlayerMove == 'r') and (ComputerMove == 'PAPER'):
        print("Aw you lost.")
        losses = (losses + 1)
    elif (PlayerMove == 'r') and (ComputerMove == 'SCISSORS'):
        print("That's a win for you!")
        wins = (wins + 1)
    elif (PlayerMove == 's') and (ComputerMove == 'PAPER'):
        print("That's a win for you!")
        wins = (wins + 1)
    elif (PlayerMove == 's') and (ComputerMove == 'ROCK'):
        print("Aw you lost.")
        losses = (losses + 1)
