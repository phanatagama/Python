import math

def square(a):
  s = int(a**0.5)
  return s*s == a
def fibo(n):
  return square(5*n*n+4) or square(5*n*n-4)
z = int(input('masukkan angka\n'))
if fibo(z) == True:
  print('ini fibonacci')
  #if z == 1:
    #print('fibo sebelumnya 1/ tidak ada')
    #print('fibo sesudahnya 1/2')
  #else:
  g = z-1
  while fibo(g) == False:
     g -= 1
  print('angka sebelumny', g)
  k = z+1
  while fibo(k) == False:
     k += 1
  print('angka sesudahnya', k)   
else:
  print('bukan fibo')

