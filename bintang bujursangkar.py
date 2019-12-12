n = int(input('masukkan banyak bintang'))
x = 1
k = n
#SEGITIGA ATAS
while n>0:
    print((n-1)*' ' + x*'*' + (x-1)*'*')
    x+=1
    n-=1
#SEGITIGA BAWAH
while n < k:
    x-=1
    print((n+1)*' ' + (x-1)*'*' + (x-2)*'*')
    n+=1
    
