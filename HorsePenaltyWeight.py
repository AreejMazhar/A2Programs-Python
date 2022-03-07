HorseName = input("Enter the name of the horse: ")
PrevWins = int(input("Enter the number of the previous wins: "))

if (PrevWins == 0):
    PenaltyWeight = 0
elif (PrevWins == 1) or (PrevWins == 2):
    PenaltyWeight = 4
elif (PrevWins > 2):
    PenaltyWeight = 8

print ("The horse " + HorseName + " has the penalty weight: " + str(PenaltyWeight))
