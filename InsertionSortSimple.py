Num = [74, 8, 4, 8, 1, 34, 12]

Maxsize = 7

for count in range(0,Maxsize):
    Temp = Num[count]
    insert = count
    while  (insert>0) and (Num[insert-1]>=Temp):
        Num[insert] = Num[insert-1]
        insert = insert -1

    Num[insert] = Temp
    Maxsize = Maxsize -1 

for count in range(0,7):
    print(count , ": " , Num[count])
