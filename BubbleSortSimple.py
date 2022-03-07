BSortArr = [107, 179, 150, 123, 105, 134, 102, 167, 101, 100]

Maxsize = 9
Swap = False
while (Swap == False):
    Swap=True
    for i in range(0,Maxsize):
        if BSortArr[i] > BSortArr[i + 1]:
            Temp = BSortArr[i]
            BSortArr[i] = BSortArr[i+1]
            BSortArr[i+1] = Temp
            Swap = False
    Maxsize = (Maxsize - 1)

for i in range(10):
    print(i, 'Number: ', BSortArr[i])
