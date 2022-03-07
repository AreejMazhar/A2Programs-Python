Num = [620, 412, 1011, 313, 505, 909, 707, 820]

Found = False
count  = 0

SearchNum = int(input("Enter the number you want to search: "))

while (Found == False) and (count < 8):
    if SearchNum == Num[count]:
        Found = True
        print ("Your number has been found at: " + str(count))
    count = count + 1

if (count == 8):
    print ("Your number is not in the array.")
