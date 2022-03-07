Player1Total = 0
Player2Total = 0

for NoOfThrows in range(5):
    Player1Throw = int(input("Enter Player 1's score"))
    Player2Throw = int(input("Enter Player 2's score"))
    if Player1Throw > Player2Throw:
        Player1Total = Player1Total + 1
    if Player2Throw > Player1Throw:
        Player2Total = Player2Total + 1

if Player1Total > Player2Total:
    print("Player1 is the winner!")
elif Player1Total < Player2Total:
    print("Player2 is the winner!")
else:
    print("It\'s a tie!")
