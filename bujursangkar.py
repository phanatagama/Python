nilai = int(input("Piramida tingkat : "))
masuk = 2
baris = 1
number = nilai
while (nilai > 0):
    angka = nilai
    if (baris % 2 == 0):
        masuk = masuk + ((2*baris)-2)
        print(angka*' ', end="")
        angka=0
        while (angka < baris):
            print(masuk, "", end="")
            masuk = masuk - 2
            angka = angka + 1
        masuk = masuk + ((2*baris)+2)
    else:
        print(angka*' ', end="")
        angka = 0
        while (angka < baris):
            print(masuk, "", end="")
            masuk += 2
            angka += 1
    nilai-= 1
    baris+= 1
    print("")
nilai = 1
while (nilai < number+1):
    angka = 0
    if (baris % 2 == 0):
        masuk = masuk + ((2*(baris-1))-2)
        print(nilai*' ', end="")
        angka=nilai
        while (angka <= number):
            print(masuk,"", end="")
            masuk = masuk - 2
            angka = angka + 1
        masuk = masuk + ((2*(baris-1))+2)   
    else:
        print(nilai*' ', end="")
        angka=nilai
        while (angka <= number):
            print(masuk,"", end="")
            masuk += 2
            angka += 1
    nilai+= 1
    baris-= 1
    print("")
