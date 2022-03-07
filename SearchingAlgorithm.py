def LinearSearch(num):
    found = False
    count = 0

    while (found == False) or (count < 9):
        if num == Numbers[count]:
            found = True
            return count
        else:
            count = count + 1
        #endif
    #endwhile
        if (count == 9):
            return -1
        #endif
#endfunction

def Bsort(Numbers):
    maxsize = 10
    swap = False

    while (swap == False):
        swap = True
        for i in range(0, (maxsize-1)):
            if Numbers[i] > Numbers[i+1]:
                temp = Numbers[i]
                Numbers[i] = Numbers[i+1]
                Numbers[i+1] = temp
                swap = False
            #endif
        #endfor
        maxsize = maxsize - 1
    #endwhile
#endprocedure

def BinarySearch(Num):
    found = False
    LB = 0
    UB = 9
    
    while (UB >= LB) and (found == False):
        mid = int((LB + UB)/2)
        if (Numbers[mid] == Num):
            found = True
            return mid
        elif (Num < Numbers[mid]):
            UB = mid - 1
        else:
            LB = mid + 1
        #endif
    #endwhile
    return -1
#endfunction

Numbers = [32, 21, 7, 48, 51, 22, 9, 15, 11, 27]

value = int(input("Enter the number you would like to search: "))
choice = input("Would you like to conduct a (L)inear or (B)inary search?: ")

if (choice == "L") or (choice == "l"):
    x = LinearSearch(value)
    if (x == -1):
        print("Sorry, your number is not in this array :(")
    else:
        print("You number was found at index: ", x)
    #endif
elif (choice == "B") or (choice == "b"):
    Bsort(Numbers)
    y = BinarySearch(value)
    if (y == -1):
        print("Sorry, your number is not in this array :(")
    else:
        print("You number was found at index: ", y)
    #endif
else:
    print("Invalid choice, program terminated.")
#endif
