alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def BinaryS(value):
    Found = False
    LB = 0
    UB = 26
    while (UB>=LB) and (Found == False):
        middle = int((LB + UB)/2)
        if alphabets[middle] == value:
            Found = True
            return middle
        elif value < alphabets[middle]:
            UB = middle - 1
        else:
            LB = middle + 1

    return -1


CharSearch = input("Enter the letter you would like to search: ")
if (BinaryS(CharSearch) != -1):
    print (CharSearch + " found at location " + str(BinaryS(CharSearch)))
else:
    print ("Not in the array, sorry.")
