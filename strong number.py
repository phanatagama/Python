n = int(input('masukkan bilangan\n'))
#for n in range(1, 9999999):
s1 = 0
j = n
while j>=1:
    fact = 1
    i = 1
    while i<=j%10:
        fact*=i
        i+=1
    s1=s1+fact
    j=j/10
if s1==n:
    print(n,'strong number')
else:
    print('bukan strong number')

