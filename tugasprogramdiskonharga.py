print('##  Program Potongan Harga  ##')
print('==============================')
print()
 
harga_asli = int(input('Harga Asli: Rp. '))
 
if (harga_asli >= 50000) and (harga_asli < 100000):
  harga_akhir = harga_asli - (0.1*harga_asli)
  print('Anda mendapat diskon 10%')
elif (harga_asli >= 100000) and (harga_asli < 500000):
  harga_akhir = harga_asli - (0.23*harga_asli)
  print('Anda mendapat diskon 23%')

  jwb = harga_asli*0.23
else:
  harga_akhir = harga_asli

print('Harga Diskon: Rp.',round(jwb,))
print('Total bayar: Rp.',round(harga_akhir,))
