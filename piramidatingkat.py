n = int(input("n = "))
x = 1
nCopy = n
baris = 1
while nCopy > 0:
    elemenBaris = 1
    bantu = 2*nCopy
    while elemenBaris <= nCopy:
        if baris % 2 == 0:
            print((x + (bantu - 2*elemenBaris)), end=" ")
            bantu -= 2
        else:
            print(x, end=" ")
        x += 2
        elemenBaris += 1
    print("\n",end="")
    nCopy -= 1
    baris += 1
nCopy = 1
while nCopy <= n:
    elemenBaris = 1
    bantu = 2*nCopy
    while elemenBaris <= nCopy:
        if baris % 2 == 0:
            print((x + (bantu - 2*elemenBaris)), end=" ")
            bantu -= 2
        else:
            print(x, end=" ")
        x += 2
        elemenBaris += 1
    print("\n",end="")
    nCopy += 1
    baris += 1

11, 9, 7, 5, 3, 1
