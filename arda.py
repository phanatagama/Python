a=0
b=1
d=0
x = int(input('masukkan'))
while d<x:
    d = a+b
    a=b
    b=d

if x==d:
    print(x, 'adalah fibonacci')
    print('sebelum', a)
    print('sesudah', a+d)
else:
    print('bukan fibo')
