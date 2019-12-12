angka = int(input('masukkin angka: '))
Total = 0
pembagi=0
#for i in range(1, n):
while angka > 0:
  pembagi+=1
  bil = 1/pembagi
  print(bil)
  simpan = Total+bil
  Total = simpan
  angka-=1
  
print('hasilnya = ', Total)
