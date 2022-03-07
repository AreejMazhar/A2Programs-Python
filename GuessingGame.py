import random

RandomNum = random.randint(1, 20)
print("I chose a number in between 1 to 20!")
GuessNum = int(input("Can you guess it?:"))

guess = 1

for count in range(5): #Player only has 6 guesses
    if (GuessNum < RandomNum):
        print("Your guess is too low!")
        GuessNum = int(input("Try Again!"))
        guess = (guess+1)
    elif (GuessNum > RandomNum):
        print("Your guess is too high!")
        GuessNum = int(input("Try Again!"))
        guess = (guess+1)
    else:
        break #if correct, breaks out of loop

if (GuessNum == RandomNum):
    print("You guessed correctly! You took " , guess, " guesses.")
else:
    print ("Sorry, you could not guess correctly :(")
    print("I chose the number ", RandomNum)
