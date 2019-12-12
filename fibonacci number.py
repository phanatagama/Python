b = 1
c = 0
n=int(input('banyak bilangan yang ingin ditampilkan: '))
while 0<n:
    a = b + c
    b = c
    c = a
    n -= 1
    print(a, end=',')
