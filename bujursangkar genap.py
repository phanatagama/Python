nilai = int(input("Piramida tingkat : "))
masuk = 2
baris = 1
number = nilai
while nilai > 0:
    angka=0
    if baris%2!=0:
        print(nilai*' ', end="")
        while (angka < baris):
            print(masuk, "", end="")
            masuk += 2
            angka += 1
    else:
        masuk = masuk + ((2*baris)-2)
        print(nilai*' ', end="")
        while (angka < baris):
            print(masuk, "", end="")
            masuk = masuk - 2
            angka = angka + 1
        masuk = masuk + ((2*baris)+2)
    nilai-= 1
    baris+= 1
    print("")
while nilai <= number:
    angka=nilai
    if baris%2 != 0:
        print(nilai*' ', end="")
        while (angka < number):
            print(masuk, "", end="")
            masuk += 2
            angka += 1
    else:
        masuk = masuk + ((2*(baris-1))-2)
        print(nilai*' ', end="")
        while (angka < number):
            print(masuk, "", end="")
            masuk = masuk - 2
            angka = angka + 1
        masuk = masuk + ((2*(baris-1))+2)
    nilai+= 1
    baris-= 1
    print("")
    

